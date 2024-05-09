# Bell SFTP Backup

Bell FTP Backup is a robust tool designed to automate the backup of files and folders through Secure File Transfer Protocol (SFTP or SCP). It ensures data safety by maintaining state across sessions, enabling resume capability after interruptions.

## Features

- **Automated Backups:** Scheduled backups to an SFTP server.
- **Stateful Transfers:** Remembers the last file transferred and resumes after any interruptions.
- **Secure:** Uses SFTP for secure transfer of data.
- **Logging:** Detailed logs for monitoring and troubleshooting.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.6+
- Paramiko (Python library)
- pymysql (Python library)
- A server with SFTP access
- MariaDB or MySQL setup for logging transfer details

## Installation

1. **Clone the Repository:**
   
   ```bash
   git clone https://github.com/yourusername/bell-sftp-backup.git
   cd bell-sftp-backup

3. **Install Required Python Libraries:**
**On Linux (Global)**

   ```bash
   pip install paramiko pymysql

**On Debian 12:**

     pip install paramiko pymysql --break-system-packages

4. **Set up Environment Variables:**
Create a .env file in the root directory of the project and update the following settings:

    ```bash
    # .ENV

   # General Debug Configuration
   # Enable or disable debug mode globally. Required to be True for any debugging features, including logging, to be active.
   DEBUG=True
   
   # Logging Configuration
   # Enable or disable all logging messages. Requires DEBUG=True to take effect. Controls whether log messages are shown.
   DEBUG_MESSAGES=True
   
   # Specific Log Level Configurations
   # These settings control the display of log messages at different levels. 
   # Each specific logging type below (ERROR, INFO, WARNING, CRITICAL) requires both DEBUG and DEBUG_MESSAGES to be True to be active.
   
   # Enable or disable error level log messages. For tracking errors. Requires DEBUG and DEBUG_MESSAGES to be True.
   DEBUG_ERROR=True
   
   # Enable or disable informational log messages. For operational insights. Requires DEBUG and DEBUG_MESSAGES to be True.
   DEBUG_INFO=True
   
   # Enable or disable warning level log messages. For potential issues. Requires DEBUG and DEBUG_MESSAGES to be True.
   DEBUG_WARNING=True
   
   # Enable or disable critical level log messages. For severe failures. Requires DEBUG and DEBUG_MESSAGES to be True.
   DEBUG_CRITICAL=True
   
   LOCAL_DIRECTORY = '/local/folder/location'  # Ensure this path is correct and accessible
   REMOTE_DIRECTORY = '/remote/folder/location'
   
   # Server host remote
   REMOTE_HOST = 'remotehost_ip'
   REMOTE_PORT = 22
   REMOTE_USERNAME = 'username'
   REMOTE_PASSWORD = 'password'
   REMOTE_PROTOCOL='sftp' # Valid values are "sftp" or "scp"
   
   # General Configuration
   USE_RELOADER=False
   SESSION_PERMANENT=True
   SESSION_USE_SIGNER=True
   ASYNC_MODE='threading'
   SECRET_KEY='your_script_secret_key'
   MAIN_DIR='/script/project/folder/location' # e.g /root/bell_backup_script
   
   SAVE_DATA_TO_DB=True # Set True or False for saving all transferred files in the db
   BBACKUP_SCHED_DB_HOST="sql_host"
   BBACKUP_SCHED_DB_USER="sql_user"
   BBACKUP_SCHED_DB_PASSWORD="sql_password"
   BBACKUP_SCHED_DB_NAME="sql_database"

5. **Database Setup:**
- Log into your MariaDB/MySQL server and create a new database.
- Execute the following SQL script to create the necessary table:
  
    ```bash
    CREATE TABLE backup_files (
      id INT AUTO_INCREMENT PRIMARY KEY,
      file_name VARCHAR(255) NOT NULL,
      file_size BIGINT NOT NULL,
      transfer_duration DOUBLE NOT NULL,
      transfer_rate DOUBLE NOT NULL,
      local_path TEXT NOT NULL,
      remote_path TEXT NOT NULL,
      transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
**Usage**
To run the Bell SFTP Backup, navigate to the project directory and execute:

      cd /path/location/bell_sftp_backup && python3 -m app

This will initiate the backup process as configured in your .env file and database settings.

**Contributing**
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

**License**
Distributed under the MIT License. See LICENSE for more information.

**Contact**
Project Link: https://github.com/bellnetwork/bell_sftp_backup
