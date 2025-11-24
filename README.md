<p align="center">
  <img src="project-banner.png" width="100%" alt="Project Banner">
</p>

# 🍽️ Recipe App – DevOps CI/CD Project  

A complete end-to-end DevOps project integrating **Docker**, **Kubernetes (Minikube)**, and **Jenkins CI/CD** for automated deployments.

---

## 🚀 Badges

<p align="center">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker">
  <img src="https://img.shields.io/badge/Kubernetes-Minikube-blue?logo=kubernetes">
  <img src="https://img.shields.io/badge/Jenkins-CI%2FCD-red?logo=jenkins">
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-green?logo=flask">
</p>

---

## 🌐 Live Demo (Optional)

> Add your live Minikube URL or cloud deployment here.  
*(If running locally, skip this section.)*

---

## 🧱 Architecture Diagram

+------------+ +-------------+ +------------------+
| Developer | ---> | GitHub | -----> | Jenkins Pipeline |
+------------+ +-------------+ +------------------+
|
v
+----------------+
| Docker Build |
+----------------+
|
v
+-------------------------+
| Minikube Kubernetes |
| Deployment (Pods/Svc) |
+-------------------------+
|
v
🍽️ User accesses Recipe App

yaml
Copy code

---

## 📌 Project Overview

This is a simple Python/Flask Recipe Application deployed using:

- **Docker** → Containerized application  
- **Kubernetes (Minikube)** → Cluster deployment  
- **Jenkins Pipeline** → CI/CD automation  
- **GitHub** → Source Code Management  

---

## 📁 Project Structure

recipe-app/
│
├── app.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── project-banner.png
├── templates/
│ ├── index.html
│ └── recipe.html
└── instance/
└── database files (if any)

yaml
Copy code

---

# 🛠️ Setup Instructions (Very Clear Step-by-Step)

## 1️⃣ Clone the Repository

```sh
git clone https://github.com/sowmiya-projects/recipe-app.git
cd recipe-app
2️⃣ Build Docker Image
sh
Copy code
docker build -t recipe-app-k8s .
3️⃣ Start Minikube
sh
Copy code
minikube start
Use Minikube Docker environment:

sh
Copy code
minikube -p minikube docker-env
4️⃣ Load Image into Minikube
sh
Copy code
minikube image load recipe-app-k8s
5️⃣ Deploy to Kubernetes
sh
Copy code
minikube kubectl -- apply -f deployment.yaml
minikube kubectl -- apply -f service.yaml
Check pods:

sh
Copy code
minikube kubectl -- get pods
Expose service:

sh
Copy code
minikube service recipe-service
⚙️ Jenkins CI/CD Pipeline
This project uses an automated Jenkins pipeline for:

Pulling latest code from GitHub

Building Docker image

Loading image into Minikube

Deploying updated version

Verifying pods

Jenkinsfile Used
groovy
Copy code
pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sowmiya-projects/recipe-app.git'
            }
        }

        stage('Use Minikube Docker') {
            steps {
                sh 'eval $(minikube -p minikube docker-env)'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t recipe-app-k8s:latest .'
            }
        }

        stage('Load Image to Minikube') {
            steps {
                sh 'minikube image load recipe-app-k8s:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'minikube kubectl -- apply -f deployment.yaml'
                sh 'minikube kubectl -- apply -f service.yaml'
            }
        }

        stage('Verify Pods') {
            steps {
                sh 'minikube kubectl -- get pods'
            }
        }
    }
}
📜 Deployment YAML Files
deployment.yaml
yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: recipe-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: recipe-app
  template:
    metadata:
      labels:
        app: recipe-app
    spec:
      containers:
        - name: recipe-app
          image: recipe-app-k8s:latest
          imagePullPolicy: Never
          ports:
            - containerPort: 5000
service.yaml
yaml
Copy code
apiVersion: v1
kind: Service
metadata:
  name: recipe-service
spec:
  type: NodePort
  selector:
    app: recipe-app
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30000
🐳 Dockerfile
dockerfile
Copy code
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
🤝 Contributing
Pull requests are welcome!
If you want new features, feel free to open an issue.

📄 License
This project is open-source and free to use.

🎉 Thank You!
If you like this project, please ⭐ star the repository!
