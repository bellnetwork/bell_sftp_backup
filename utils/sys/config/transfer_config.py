# Transfer config.py

from dotenv import load_dotenv
import os

def get_config():
    # Load environment variables from .env file
    load_dotenv()

    return {
        'debug': os.getenv('DEBUG', 'False').lower() in ['true', '1', 't'],
        'engineio_logger': os.getenv('ENGINEIO_LOGGER', 'False').lower() in ['true', '1', 't'],
        'remote_host': os.getenv('REMOTE_HOST'),
        'remote_port': int(os.getenv('REMOTE_PORT')),
        'remote_user': os.getenv('REMOTE_USERNAME'),
        'remote_passwd': os.getenv('REMOTE_PASSWORD'),
        'remote_protocol': os.getenv('REMOTE_PROTOCOL'),
        'local_directory': os.getenv('LOCAL_DIRECTORY'),
        'remote_directory': os.getenv('REMOTE_DIRECTORY'),
        'bbackup_sched_db_host': os.getenv('BBACKUP_SCHED_DB_HOST'),
        'bbackup_sched_db_user': os.getenv('BBACKUP_SCHED_DB_USER'),
        'bbackup_sched_db_password': os.getenv('BBACKUP_SCHED_DB_PASSWORD'),
        'bbackup_sched_db_name': os.getenv('BBACKUP_SCHED_DB_NAME'),
        'db_save_status': os.getenv('SAVE_DATA_TO_DB', 'False').lower() in ['true', '1', 't']
    }
