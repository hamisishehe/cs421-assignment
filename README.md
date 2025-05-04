Software Engineering API - Flask API
This project is a Flask-based API designed to provide information about students and subjects associated with a Software Engineering program. The API includes two main endpoints:

/students: Provides a list of students and their enrolled programs.

/subjects: Lists subjects for the Software Engineering program, organized by academic year.

🌐 API Live Links:

http://3.148.192.1:5000/subjects


http://3.148.192.1:5000/students

Bash Scripts (bash_scripts/ Directory)
This folder contains Bash scripts to help monitor, back up, and maintain the API server.

## 1. health_check.sh
Checks CPU, memory, and disk usage.

Verifies the web server is running.

Tests /students and /subjects API endpoints.

Logs status to /var/log/server_health.log.

## 2. backup_api.sh
Backs up the API project files and MySQL database.

Archives are stored in ~/backups.

Automatically deletes backups older than 7 days.

Logs status to /var/log/backup.log.

## 3. update_server.sh
Updates Ubuntu packages.

Pulls the latest changes from GitHub.

Restarts the web server.

Logs to /var/log/update.log.

How to Use Bash Scripts:
bash
Copy
Edit
# Make scripts executable
chmod +x bash_scripts/*.sh

# Run a script
./bash_scripts/health_check.sh
Docker Deployment
Building Docker Images
Inside your project directory (hamisi-api/):

bash
Copy
Edit
# Build the Docker images using Docker Compose
sudo docker-compose build
This will create:

hamisi-api_api:latest — Your Flask API container.

mysql:8.0 — The MySQL database container.

Running the Containers
bash
Copy
Edit
# Run containers in the background
sudo docker-compose up -d
You can view running containers with:

bash
Copy
Edit
docker ps
Viewing Container Logs
bash
Copy
Edit
docker logs <container_name>
Example:

bash
Copy
Edit
docker logs hamisi-api_api_1
Docker Registry Upload
1. Tag Your Image (if needed)
If you have not already tagged:

bash
Copy
Edit
docker tag hamisi-api_api hamisishehe05/hamisi-api:latest
2. Login to Docker Hub
bash
Copy
Edit
docker login
Enter your Docker Hub username and password.

3. Push the Image
bash
Copy
Edit
docker push hamisishehe05/hamisi-api:latest
This uploads your image to Docker Hub.

## Docker Hub Link
You can pull the image using:

bash
Copy
Edit
docker pull hamisishehe05/hamisi-api:latest
Or view it on Docker Hub:
👉 https://hub.docker.com/r/hamisishehe05/hamisi-api


Troubleshooting Tips and Problem	Solution
->Error starting userland proxy: listen tcp4 0.0.0.0:3306: bind: address already in use	MySQL is already running on port 3306. Stop it: sudo systemctl stop mysql
->denied: requested access to the resource is denied	You forgot to docker login before pushing images.
->Flask server accessible on localhost but not public IP	Make sure Flask binds to 0.0.0.0 and EC2 Security Group allows port 8000 or 5000.
Docker Compose not recognized	Install Docker Compose: sudo apt install docker-compose


## Project Dependencies
Make sure these are installed on the server:

curl

tar

mysqldump (or your database client)

git

docker

docker-compose




#  Containerized Frontend with Load Balancer

This project includes a Flask backend (`api`), three frontend instances (`frontend1`, `frontend2`, `frontend3`), a MySQL database (`db`), and an Nginx load balancer, all containerized using Docker Compose.

---

##  Instructions to Build and Run Front-End Containers

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hamisishehe/cs421-assignment.git
   cd your-repo
   ```

2. **Build the Containers:**

   ```bash
   docker-compose build
   ```

   Or build and run in one command:

   ```bash
   docker-compose up --build
   ```

3. **Start the Services:**

   ```bash
   docker-compose up
   ```

4. **Access the Front-End via Load Balancer:**

   ```
   http://3.148.192.1/
   ```

   You can also directly access the individual frontends:

   * `http://3.148.192.1:3000`
   * `http://3.148.192.1:3001`
   * `http://3.148.192.1:3003`

---

## ⚙️ Load Balancer Setup

The project uses **Nginx (alpine)** as a load balancer to distribute traffic between three frontend containers using a **round-robin algorithm**.

### Load Balancing Details:

* **Algorithm**: Round-robin (default Nginx behavior)
* **Load Balanced Containers**: `frontend1`, `frontend2`, `frontend3`
* **Port**: Listens on port `80` on the host machine

###  Health Checks:

Basic health checks are handled by Docker. Nginx can be configured to skip failed servers using upstream failover logic.

Example (not included by default):

```nginx
proxy_next_upstream error timeout http_502 http_503 http_504;
```

---

## ☁️ Deploying on AWS

1. **Launch an EC2 instance**

   * Recommended OS: Ubuntu or Amazon Linux 2
   * Open ports: `80`, `3000`, `3001`, `3003`, `5000`

2. **Install Docker and Docker Compose**

   ```bash
   sudo apt update
   sudo apt install docker.io docker-compose -y
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

3. **Clone the Repository:**

   ```bash
   git clone https://github.com/hamisishehe/cs421-assignment.git
   cd your-repo
   ```

4. **Build and Run the App:**

   ```bash
   sudo docker-compose up --build -d
   ```

5. **Access the Application via Public IP:**

   * Load Balanced Frontend: `http://<EC2-PUBLIC-IP>/`
   * Flask API: `http://<EC2-PUBLIC-IP>:5000`

---

## 💠 Troubleshooting Tips

| Issue                       | Solution                                                                |
| --------------------------- | ----------------------------------------------------------------------- |
|  Front-end not loading    | Check `docker ps`. Ensure all frontend containers are running.          |
|  API not connecting to DB | Check `docker-compose logs db`. Ensure the DB is healthy and ready.     |
|  Nginx errors              | Check `docker-compose logs nginx`. Verify `nginx.conf` routing.         |
|  Header not appearing     | Confirm frontend assets are loading. Check browser dev tools.           |
|  Flask API crashing       | Run `docker-compose logs api`. Check for missing packages or DB issues. |

---


