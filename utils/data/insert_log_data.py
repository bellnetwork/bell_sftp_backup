# Insert Log data.py
from utils.database.database_handler import execute_bbackup_sched_sql_query

def insert_backup_files_data(file_name, file_size, transfer_duration, transfer_rate, local_path, remote_path):
    sql = "INSERT INTO backup_files (file_name, file_size, transfer_duration, transfer_rate, local_path, remote_path) VALUES (%s, %s, %s, %s, %s, %s)"
    execute_bbackup_sched_sql_query(query=sql, params=(file_name, file_size, transfer_duration, transfer_rate, local_path, remote_path))