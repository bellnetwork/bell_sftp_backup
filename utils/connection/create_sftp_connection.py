# Create Transfer connection.py

import paramiko
from paramiko import SSHClient
from scp import SCPClient
from utils.sys.sys_messages.logging import *
from utils.sys.config.transfer_config import *

config = get_config()

async def create_sftp_client():
    """Creates an SFTP or SCP client based on configuration and returns it."""
    try:
        transport = paramiko.Transport((config['remote_host'], config['remote_port']))
        transport.connect(username=config['remote_user'], password=config['remote_passwd'])

        if config['remote_protocol'] == 'sftp':
            sftp = paramiko.SFTPClient.from_transport(transport)
            setup_custom_logging('info', __name__, 'SFTP connection established.')
            return sftp
        elif config['remote_protocol'] == 'scp':
            scp = SCPClient(transport)
            setup_custom_logging('info', __name__, 'SCP connection established.')
            return scp
    except paramiko.SSHException as e:
        setup_custom_logging('error', __name__, f'Failed to create file transfer client: {e}')
        return None
