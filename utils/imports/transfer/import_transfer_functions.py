# Import the event handler imports module
from utils.imports.function_handler_imports import create_sftp_client, transfer_folder, save_state, load_state

def setup_all_transfer_events():
    """Sets up all transfer-related events by calling all required functions."""
    create_sftp_client()
    transfer_folder()
    save_state()
    load_state()