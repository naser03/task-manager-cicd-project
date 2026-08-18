# 🚀 Task Manager — DevOps CI/CD Project

A containerized Task Manager application demonstrating an end-to-end DevOps workflow using **Git, GitHub, Docker, Docker Compose, Docker Hub, GitHub Actions, AWS EC2, Linux, and Nginx**.

The project focuses on containerization, Docker networking, reverse proxy configuration, image management, and automated deployment to AWS EC2.

## 🏗️ Architecture

Developer
    │
    │ git push
    ▼
 GitHub
    │
    ▼
GitHub Actions
    │
    ├── Build Docker Images
    ├── Push Images
    │
    ▼
Docker Hub
    │
    │ pull
    ▼
 AWS EC2
    │
    ▼
Docker Compose
    │
    ▼
   Nginx
    │
    ├──────────────┐
    ▼              ▼
Frontend         Backend
 :80             :5000
                    │
                    ▼
                Flask API

## 🏗️ Complete Deployment Flow

1. Developer writes code
          ↓
2. git push
          ↓
3. GitHub Actions starts
          ↓
4. Docker images are built
          ↓
5. Images pushed to Docker Hub
          ↓
6. GitHub Actions connects to EC2
          ↓
7. EC2 pulls latest images
          ↓
8. Docker Compose recreates containers
          ↓
9. Nginx routes traffic
          ↓
10. Application is live