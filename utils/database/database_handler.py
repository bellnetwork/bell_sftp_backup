# Database handler.py

import pymysql, json, os
from utils.sys.sys_messages.logging import *
from utils.sys.config.transfer_config import *

config = get_config()

# Connect to bbackup_sched database
def bbackup_sched_connect_database():
    return pymysql.connect(
        host=config['bbackup_sched_db_host'],
        user=config['bbackup_sched_db_user'],
        password=config['bbackup_sched_db_password'],
        db=config['bbackup_sched_db_name'],
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

# Function to execute SQL queries and fetch data
def execute_bbackup_sched_sql_query(query, params=None):
    if config['db_save_status']:  # No need to compare explicitly to True
        connection = bbackup_sched_connect_database()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()  # This assumes a SELECT; adjust if performing INSERT/UPDATE
            connection.commit()
        finally:
            connection.close()
        return result
    else:
        setup_custom_logging('info', __name__, 'Database saving is disabled.')
        return None  # Explicitly return None