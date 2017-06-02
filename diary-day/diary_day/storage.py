import sqlite3
import os.path as Path
conn = sqlite3.connect('diary.db')

c = conn.cursor()

sql = '''
    CREATE TABLE IF NOT EXISTS diary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL DEFAULT '',
        task_text TEXT NOT NULL DEFAULT '',
        task_status TEXT NOT NULL DEFAULT ''     
    )
'''

c.execute(sql)

SQL_SELECT_ALL = '''
    SELECT
        id, task_name, task_text, task_status
    FROM
        diary
'''

SQL_SELECT_BY_ID = '''
    SELECT
        id, task_name, task_text, task_status
    FROM
        diary
    WHERE id = %s
'''

SQL_NEW_TASK = '''
    INSERT INTO diary (task_name, task_text, task_status)
    VALUES('%s', '%s', '%s')
    
'''

SQL_REDACTION = '''
    UPDATE diary 
    SET task_name = '%s', task_text = '%s', task_status = '%s'
    WHERE ID = %s
'''

SQL_CLOSING = '''
    UPDATE diary 
    SET task_status = 'выполнено'
    WHERE ID = %s
'''


def find_all(conn):
    with conn:
        c = conn.execute(SQL_SELECT_ALL)
        return c.fetchall()

def add_task(conn, task_name, task_text, task_status):
    with conn:
        c = conn.execute(SQL_NEW_TASK % (task_name, task_text, task_status))

def redact_task(conn, id, task_name, task_text, task_status):
    with conn:
        c = conn.execute(SQL_REDACTION % (task_name, task_text, task_status, id))

def close_task(conn, id):
    with conn:
        c = conn.execute(SQL_CLOSING % id)
                                

def check_row_exists(conn, id):
    with conn:
        c = conn.execute(SQL_SELECT_BY_ID % id)
        obj = c.fetchall()
        if len(obj) == 0:
            return False
        else:
            return True
