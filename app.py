# cd /root/bell_backup && python3 -m app
# pip install paramiko

import asyncio
from utils.connection.create_sftp_connection import *
from functions.transfer.transfer_folder import *
from utils.sys.sys_messages.logging import *

async def main():
    setup_custom_logging('info', __name__, 'Starting async file transfer process.')

    sftp = await create_sftp_client()
    if sftp:
        await transfer_folder(sftp)
        sftp.close()
        setup_custom_logging('info', __name__, 'Transfer complete and connection closed.')
    else:
        setup_custom_logging('error', __name__, 'Connection failed.')

if __name__ == "__main__":
    asyncio.run(main())