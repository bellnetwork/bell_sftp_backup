# Create SFTP connection.py
import paramiko
from utils.sys.sys_messages.logging import setup_custom_logging
from utils.sys.config.transfer_config import get_config
config = get_config()

async def create_sftp_client():
    """Creates an SFTP client and returns it."""
    try:
        transport = paramiko.Transport((config['remote_host'], config['remote_port']))
        transport.connect(username=config['remote_user'], password=config['remote_passwd'])
        sftp = paramiko.SFTPClient.from_transport(transport)
        setup_custom_logging('info', __name__, 'SFTP connection established.')
        return sftp
    except paramiko.SSHException as e:
        setup_custom_logging('error', __name__, f'Failed to create SFTP client: {e}')
        return None
