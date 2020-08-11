from config.config import DATABASE_CONN_STR
from db.dbHandler import DBHandler
from db.repository import Repository
from policyEngine.models.models import Whitelist, Blacklist


class RuleRepository(Repository):

    def __init__(self, obj):
        db = DBHandler(DATABASE_CONN_STR)
        super(RuleRepository, self).__init__(obj, db)


class WhitelistRepository(RuleRepository):

    def __init__(self):
        super(WhitelistRepository, self).__init__(Whitelist)


class BlacklistRepository(RuleRepository):

    def __init__(self):
        super(BlacklistRepository, self).__init__(Blacklist)






