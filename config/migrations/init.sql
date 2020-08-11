CREATE TABLE IF NOT EXISTS whitelist (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "type" TEXT NOT NULL,
    "value" TEXT NOT NULL,
    UNIQUE ("type", "value")
);

CREATE TABLE IF NOT EXISTS blacklist (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "type" TEXT  NOT NULL,
    "value" TEXT NOT NULL,
    UNIQUE ("type", "value")
);

DELETE FROM whitelist;
delete from sqlite_sequence where name='whitelist';

DELETE FROM blacklist;
delete from sqlite_sequence where name='blacklist';
