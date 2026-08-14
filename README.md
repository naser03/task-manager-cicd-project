# DevOps Task Manager — Frontend + Backend Only

A beginner-friendly full-stack project for practicing a complete CI/CD pipeline.

## Architecture

Browser
  |
  v
Frontend (Nginx + HTML/CSS/JS)
  |
  | /api/*
  v
Backend (Python + Flask + Gunicorn)

There is NO database service.

The backend stores tasks in memory. Restarting the backend clears the tasks.

## Services

### Frontend
- HTML
- CSS
- Vanilla JavaScript
- Nginx
- Docker

### Backend
- Python
- Flask
- Gunicorn
- pytest
- Docker

### DevOps
- Git
- GitHub
- Docker
- Docker Compose
- GitHub Actions
- GitHub Container Registry
- AWS EC2
- Nginx

## Project Structure

```text
two-service-devops-project/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_app.py
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── style.css
│   ├── nginx.conf
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── .gitignore
├── docker-compose.yml
└── README.md
```

# 1. Run locally

## Backend

Windows:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Linux/macOS:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Backend:

```text
http://localhost:5000
```

Health check:

```text
http://localhost:5000/api/health
```

## Frontend

Open `frontend/index.html` directly for a quick UI preview, but API functionality requires the frontend to be served through Nginx or a local web server.

# 2. Run both services with Docker Compose

From the project root:

```bash
docker compose up --build
```

Open:

```text
http://localhost:8080
```

Architecture:

```text
localhost:8080
      |
      v
Frontend container
      |
      | /api/*
      v
Backend container:5000
```

The frontend Nginx configuration proxies `/api/` to the backend service.

## Useful commands

```bash
docker compose ps
docker compose logs
docker compose logs frontend
docker compose logs backend
docker compose down
docker compose up -d
```

# 3. Test the backend

```bash
cd backend
pytest -q
```

# 4. Git workflow

Create a GitHub repository and push:

```bash
git init
git add .
git commit -m "Initial full stack application"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY
git push -u origin main
```

# 5. CI pipeline

Every push to `main` and every pull request runs:

```text
Checkout
   |
Setup Python
   |
Install dependencies
   |
Run pytest
   |
Build backend Docker image
   |
Build frontend Docker image
```

This teaches the basic CI loop before deployment.

# 6. CD pipeline

The included CD workflow demonstrates the deployment stage after CI succeeds.

For a real AWS deployment, configure these GitHub repository secrets:

```text
EC2_HOST
EC2_USER
EC2_SSH_KEY
```

The EC2 server should contain the project and have Docker + Docker Compose installed.

A production deployment flow can then become:

```text
Developer
   |
   | git push
   v
GitHub
   |
   v
GitHub Actions
   |
   +---- pytest
   |
   +---- Docker build
   |
   v
GitHub Container Registry
   |
   v
AWS EC2
   |
   +---- frontend container
   |
   +---- backend container
```

# 7. Beginner DevOps progression

Do these in order.

## Level 1 — Application

- [ ] Run backend locally
- [ ] Open the frontend
- [ ] Understand GET/POST/PATCH/DELETE
- [ ] Understand the frontend-to-backend request

## Level 2 — Git

- [ ] Create GitHub repository
- [ ] Push the project
- [ ] Create a branch
- [ ] Make a change
- [ ] Create a pull request
- [ ] Merge into main

## Level 3 — Docker

- [ ] Understand the frontend Dockerfile
- [ ] Understand the backend Dockerfile
- [ ] Build both images
- [ ] Run both containers manually
- [ ] Understand Docker networks
- [ ] Run everything with Docker Compose

## Level 4 — CI

- [ ] Understand GitHub Actions YAML
- [ ] Run automated tests
- [ ] Build Docker images in CI
- [ ] Make a failing test and observe the pipeline fail
- [ ] Fix it and push again

## Level 5 — Container Registry

- [ ] Create a GitHub Container Registry package
- [ ] Push frontend image
- [ ] Push backend image
- [ ] Tag images with Git SHA
- [ ] Understand `latest` vs immutable tags

## Level 6 — AWS

- [ ] Create an Ubuntu EC2 instance
- [ ] Configure the security group
- [ ] Install Docker
- [ ] Install Docker Compose
- [ ] Clone the repository
- [ ] Start both services
- [ ] Access the application through the EC2 public IP

## Level 7 — Automated Deployment

- [ ] Configure GitHub Secrets
- [ ] Connect GitHub Actions to EC2
- [ ] Pull new images
- [ ] Stop old containers
- [ ] Start new containers
- [ ] Verify the health endpoint

## Level 8 — Production improvements

- [ ] Add Nginx HTTPS
- [ ] Add a domain
- [ ] Add environment variables
- [ ] Add application logs
- [ ] Add Docker health checks
- [ ] Add deployment rollback
- [ ] Add monitoring
- [ ] Add resource limits

# Resume project title

**Containerized Full-Stack Task Manager with Automated CI/CD**

Example resume bullets:

- Built and containerized a two-service full-stack task management application using Docker, Docker Compose, Flask, Nginx and vanilla JavaScript.
- Implemented GitHub Actions CI to automatically run backend tests and build frontend/backend Docker images on every pull request and main-branch push.
- Designed a deployment workflow targeting AWS EC2 with separate frontend and backend containers, health checks and automated container updates.

