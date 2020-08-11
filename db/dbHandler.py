from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.exceptions import *
from db.consts import *

Session = sessionmaker()


class DBHandler(object):

    def __init__(self, conn_string):
        try:
            self._engine = create_engine(conn_string)
            Session.configure(bind=self._engine)
        except Exception:
            raise SessionBindingException(SESSION_BINDING_FAIL_LOG.format(conn_string))

    def find_all(self, model):
        """
        Find all objects of the given model
        :param model: data model
        :return: object of type model
        """
        session = Session()
        try:
            objects = session.query(model).all()
        except Exception:
            session.roleback()
            raise ExecutionFailedException(FIND_ALL_FAIL_LOG.format(model=model.__name__))
        finally:
            session.close()
        return objects

    def find(self, model, **kwargs):
        """
        Finds the all object in the DB matching the given filter and return the first
        :param model: data model
        :param kwargs: filter options
        :return: object of type model
        """
        session = Session()
        try:
            objects = session.query(model).filter_by(**kwargs).first()
        except Exception:
            session.roleback()
            raise ExecutionFailedException(FIND_FAIL_LOG.format(model=model.__name__, arguments=kwargs))
        finally:
            session.close()
        return objects

    def store(self, obj):
        """
        Storing the given obj in the DB
        :param obj: object to store
        """
        session = Session()
        try:
            objects = session.add(obj)
            session.commit()
        except Exception:
            session.roleback()
            raise ExecutionFailedException(STORE_FAIL_LOG.format(obj.__name__, obj))
        finally:
            session.close()
        return objects




