# Bell SFTP Backup

Bell SFTP Backup is a robust tool designed to automate the backup of files and folders through Secure File Transfer Protocol (SFTP). It ensures data safety by maintaining state across sessions, enabling resume capability after interruptions.

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
   
   ```bash
   pip install paramiko pymysql

4. **Set up Environment Variables:**
Create a .env file in the root directory of the project and update the following settings:

    ```bash
    DEBUG=True
    ENGINEIO_LOGGER=True
    REMOTE_HOST='example.com'
    REMOTE_PORT=22
    REMOTE_USERNAME='user'
    REMOTE_PASSWORD='password'
    LOCAL_DIRECTORY='/path/to/local/backup'
    REMOTE_DIRECTORY='/path/to/remote/backup'
    BBACKUP_SCHED_DB_HOST='localhost'
    BBACKUP_SCHED_DB_USER='dbuser'
    BBACKUP_SCHED_DB_PASSWORD='dbpassword'
    BBACKUP_SCHED_DB_NAME='dbname'
    SAVE_DATA_TO_DB=True

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

      cd /root/bell_backup && python3 -m app

This will initiate the backup process as configured in your .env file and database settings.

**Contributing**
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

**License**
Distributed under the MIT License. See LICENSE for more information.

**Contact**
Project Link: https://github.com/bellnetwork/bell_sftp_backup
