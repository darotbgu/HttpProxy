PORT = 8000

# DB
DATABASE_FILE_PATH = "proxy.db"
DATABASE_CONN_STR = "sqlite:///{path}".format(path=DATABASE_FILE_PATH)
WHITELIST_TABLE = "whitelist"
BLACKLIST_TABLE = "blacklist"

INIT_MIGRATE_PATH = "config/migrations/init.sql"

# POLICY RULES
RULES_FILE_PATH = "config/policy_rules.json"
