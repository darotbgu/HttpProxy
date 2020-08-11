from sqlalchemy import Column, Integer, Text, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Enum

from policyEngine.models.ruleType import RuleType

Base = declarative_base()

# @as_declarative()
# class Rule(object):
#     @declared_attr
#     def __tablename__(cls):
#         return cls.__name__.lower()
#
#     id = Column(Integer, primary_key=True)
#     type = Column(Enum(RuleType))
#     value = Column(Text)
#
#     __table_args__ = (UniqueConstraint('type', 'value', name='Unique {0} rule'.format(__tablename__)),)


class Whitelist(Base):
    __tablename__ = 'whitelist'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(RuleType))
    value = Column(Text)

    __table_args__ = (UniqueConstraint('type', 'value', name='Unique {0} rule'.format(__tablename__)),)


class Blacklist(Base):
    __tablename__ = 'blacklist'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(RuleType))
    value = Column(Text)

    __table_args__ = (UniqueConstraint('type', 'value', name='Unique {0} rule'.format(__tablename__)),)
