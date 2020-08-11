import sqlite3

from db.exceptions import ExecutionFailedException

SCRIPT_EXECUTION_FAILED_LOG = "Failed to execute script in db={db}, script:\n {script}"
IO_ERROR_LOG = "Failed to open script file {0}"
FILE_ERROR_LOG = "Failed to read file {0}"


def execute_sql_script_sqlite(db_path, script_path):
    """
    Execute the sql script in an sqlite database
    :param db_path: sqlite database path
    :param script_path: sql script file path
    """
    try:
        with open(script_path, 'r') as script:
            sql_script = script.read()
    except IOError:
        raise IOError(IO_ERROR_LOG.format(script))
    except Exception:
        raise Exception(FILE_ERROR_LOG.format(script))

    if sql_script:
        try:
            with sqlite3.connect(db_path, uri=True) as conn:
                cursor = conn.cursor()
                cursor.executescript(sql_script)
        except sqlite3.Error:
            raise ExecutionFailedException(SCRIPT_EXECUTION_FAILED_LOG.format(db=db_path, script=sql_script))




