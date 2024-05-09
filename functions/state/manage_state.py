# Manage state.py
import pickle
import os
from utils.sys.sys_messages.logging import setup_custom_logging

STATE_FILE = 'transfer_state.pkl'

def save_state(transferred_files):
    """Saves the state to a file."""
    with open(STATE_FILE, 'wb') as f:
        pickle.dump(transferred_files, f)
    setup_custom_logging('info', __name__, 'State saved.')

def load_state():
    """Loads the state from a file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'rb') as f:
            return pickle.load(f)
    return set()
