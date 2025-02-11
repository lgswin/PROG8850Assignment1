# Explain the script’s logic, focusing on how it connects to the MySQL database and ensures a unique filename for each backup.
import os
import subprocess
import datetime

# MySQL container details
container_name = "mysql_container"
db_name = "assignment1"  # Database to be backed up
backup_dir = "./backups"  # Local directory for storing backups
container_backup_dir = "/tmp"  # Directory inside the container to store backups

# Generate a unique backup filename with timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"{db_name}_backup_{timestamp}.sql"
container_backup_path = f"{container_backup_dir}/{backup_filename}"  # Backup path inside the container
local_backup_path = os.path.join(backup_dir, backup_filename)  # Backup path on the local machine

# Ensure the local backup directory exists
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

try:
    # Create a database backup inside the Docker container
    print(f"🚀 Creating backup inside Docker container: {backup_filename}")
    backup_command = f"docker exec {container_name} sh -c 'mysqldump -u root -p\"rootpassword\" {db_name} > {container_backup_path}'"
    subprocess.run(backup_command, shell=True, check=True)

    # Copy the backup file from the container to the local machine
    print("📂 Copying backup file to the local machine...")
    subprocess.run(f"docker cp {container_name}:{container_backup_path} {local_backup_path}", shell=True, check=True)

    print(f"Backup completed successfully! File saved at: {local_backup_path}")

except subprocess.CalledProcessError as e:
    print(f"Error during database backup: {e}")