Software Engineering API - Flask Api
This project is a Flask-based API designed to provide information about students and subjects associated with a Software Engineering program. The API includes two main endpoints:

/students: Provides a list of students and their enrolled programs.
/subjects: Lists subjects for the Software Engineering program, organized by academic year.



bash_scripts/ Directory
This folder contains Bash scripts to help monitor, back up, and maintain the API server.


health_check.sh
Checks CPU, memory, disk usage.

Verifies the web server is running.

Tests /students and /subjects API endpoints.

Logs status to /var/log/server_health.log.

backup_api.sh
Backs up the API project files and MySQL database.

Archives are stored in ~/backups.

Automatically deletes backups older than 7 days.

Logs status to /var/log/backup.log.

update_server.sh
Updates Ubuntu packages.

Pulls latest changes from GitHub.

Restarts the web server.

Logs to /var/log/update.log.


# Make scripts executable
chmod +x bash_scripts/*.sh

# Run a script
./bash_scripts/health_check.sh



Dependencies
Ensure the following tools are installed:

curl

tar

mysqldump (or your DB client)

git

For XAMPP users: /opt/lampp/bin/mysql, /opt/lampp/bin/mysqldump
