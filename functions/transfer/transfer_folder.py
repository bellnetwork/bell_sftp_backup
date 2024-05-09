# Transfer folder and files via SFTP.py
import os
import time
from functions.state.manage_state import save_state, load_state
from utils.data.insert_log_data import insert_backup_files_data
from utils.sys.sys_messages.logging import setup_custom_logging
from utils.sys.config.transfer_config import get_config
config = get_config()

async def transfer_folder(sftp):
    """Transfers a folder asynchronously via SFTP."""
    transferred_files = load_state()
    total_size_transferred = 0
    file_count = 0
    folder_count = 0
    start_time = time.time()

    for root, dirs, files in os.walk(config['local_directory']):
        relative_path = os.path.relpath(root, config['local_directory'])
        remote_root = os.path.join(config['remote_directory'], relative_path) if relative_path != '.' else config['remote_directory']
        folder_count += 1

        # Ensure remote directory exists
        try:
            sftp.listdir(remote_root)
        except IOError:
            sftp.mkdir(remote_root)
            setup_custom_logging('info', __name__, f'Created remote directory {remote_root}.')

        for file in files:
            local_path = os.path.join(root, file)
            remote_path = os.path.join(remote_root, file)
            if local_path not in transferred_files:
                file_size = os.path.getsize(local_path)
                file_start_time = time.time()
                try:
                    sftp.put(local_path, remote_path)
                    file_transfer_duration = time.time() - file_start_time
                    transfer_rate = (file_size / file_transfer_duration) / (1024 * 1024)  # MB/s
                    transferred_files.add(local_path)
                    save_state(transferred_files)
                    file_count += 1
                    total_size_transferred += file_size

                    # Call to insert data into the database
                    insert_backup_files_data(file, file_size, file_transfer_duration, transfer_rate, local_path, remote_path)

                    setup_custom_logging('info', __name__, f'Transferred {local_path} ({file_size / (1024 * 1024):.2f} MB) to {remote_path}.')
                except (IOError, OSError) as e:
                    setup_custom_logging('error', __name__, f'Failed to transfer {local_path}: {e}')
                    break

    total_time = time.time() - start_time
    setup_custom_logging('info', __name__, f'Transferred {file_count} files in {folder_count} folders, total size {total_size_transferred / (1024 * 1024):.2f} MB in {total_time:.2f} seconds.')
