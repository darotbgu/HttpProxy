import json
import logging

from policyEngine.consts import *
from policyEngine.models.models import Whitelist, Blacklist
from policyEngine.models.ruleType import RuleType
from policyEngine.repository import WhitelistRepository, BlacklistRepository


class PolicyEngine(object):

    _logger = logging.getLogger(__name__)

    def __init__(self):
        self._whitelist = WhitelistRepository()
        self._blacklist = BlacklistRepository()

    def should_access(self, values):
        """
        Check if according to the given values the policy allows access
        :param values: values
        :return: True if access is granted
        """
        allowed = False

        for rule_type, value in values.items():
            if self.blocked(rule_type, value):
                self._logger.debug(BLOCKED_LOG.format(rule_type=rule_type, value=value))
                return False
            allowed = allowed or self.allowed(rule_type, value)
        return allowed

    def blocked(self, rule_type, value):
        """
        Check if there is a rule of the given types which blocks the given value
        :param rule_type: rule type
        :param value: value
        :return: True if there is a blocking rule
        """
        result = self._blacklist.find(type=rule_type, value=value)
        return True if result else False

    def allowed(self, rule_type, value):
        """
        Check if there is a rule of the given types which allows the given value
        :param rule_type: rule type
        :param value: value
        :return: True if there is an allowing rule
        """
        result = self._whitelist.find(type=rule_type, value=value)
        return True if result else False

    def load_rules_from_json_file(self, path):
        """
        Loading the rules to the db from file in path
        :param path: file path
        """
        self._logger.info(LOADING_RULES_LOG)
        rules = self._read_rules_from_file(path)
        for rule in rules:
            rule_type = rule[TYPE_KEY]
            value = rule[VALUE_KEY]
            if rule[ALLOW_KEY]:
                self._whitelist.store(Whitelist(type=RuleType[rule_type], value=value))
            else:
                self._blacklist.store(Blacklist(type=RuleType[rule_type], value=value))

    @staticmethod
    def _read_rules_from_file(path):
        """
        Read content of the given rules json file path
        :param path: file path
        :return: rules dictionary
        """
        try:
            with open(path, 'r') as rules_config:
                rules = json.load(rules_config)
        except IOError:
            raise IOError("Failed to open rules json file {0}".format(path))
        except json.JSONDecodeError as e:
            raise ValueError("Failed to decode JSON:\n{0}".format(e.msg))
            pass
        return rules
