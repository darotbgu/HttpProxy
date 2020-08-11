class DBException(Exception):
    """ Base class for DB related Exceptions """
    pass


class ExecutionFailedException(DBException):
    """ Failed to execute DB query """
    pass


class SessionBindingException(DBException):
    """ Failed to bind session to engine """
    pass
