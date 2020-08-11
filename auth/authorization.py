import functools

from tornado.web import HTTPError

from auth.requestData import RequestData
from policyEngine.engine import PolicyEngine
from policyEngine.models.ruleType import RuleType


def authorized(func):
    @functools.wraps(func)
    def wrapper(request_handler, host, port, *args, **kwargs):
        policy_engine = PolicyEngine()
        if not _has_permission(request_handler.request, host, port, policy_engine):
            raise HTTPError(401)
        return func(request_handler, host, port, *args, **kwargs)
    return wrapper


def _has_permission(request, host, port, policy_engine):
    """
    Gets the check if the policy engine allows access
    :param request: incoming HTTP request
    :param host: remote host
    :param port: remote port
    :param policy_engine: policy engine instance
    :return: True if access is allowed by policy
    """
    values = _get_rules_values(request, host, port)
    return policy_engine.should_access(values)


def _get_rules_values(request, host, port):
    """
    Extracting relevant data from the request for each RuleType
    :param request: incoming HTTP request
    :param host: remote host
    :param port: remote port
    :return: Matching Request values for the rules
    """
    request_data = RequestData(request,  host, port)

    # TODO: add a better authentication for the source user
    if not request_data.source_user:
        # It is not possible accessing anonymously
        raise HTTPError(401)

    values = {
        RuleType.SOURCE_IP: request_data.source_ip,
        RuleType.SOURCE_USER: request_data.source_user,
        RuleType.DESTINATION_HOST: request_data.destination_host,
        RuleType.DESTINATION_PORT: request_data.destination_port,
        RuleType.DESTINATION_METHOD: request_data.method,
    }
    return values



