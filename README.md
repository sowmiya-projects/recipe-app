<p align="center">
  <img src="project-banner.png" width="100%" alt="Project Banner">
</p>

# 🍽️ Recipe App – DevOps CI/CD Project  
*A complete end-to-end DevOps project integrating Docker, Kubernetes (Minikube), and Jenkins CI/CD.*

---
## 🚀 Badges

<p align="center">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker">
  <img src="https://img.shields.io/badge/Kubernetes-Minikube-blue?logo=kubernetes">
  <img src="https://img.shields.io/badge/Jenkins-CI%2FCD-red?logo=jenkins">
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-green?logo=flask">
</p>

## 🚀 Project Overview

This is a simple Python/Flask Recipe Application deployed using:

- **Docker** – Containerized application  
- **Kubernetes (Minikube)** – Cluster deployment  
- **Jenkins Pipeline** – CI/CD automation  
- **GitHub** – Version Control  

This project demonstrates full DevOps lifecycle automation from code → build → image → deploy → verify.

---

## 📌 Features

✔ REST API + UI for recipe app  
✔ Docker containerization  
✔ Kubernetes deployment with Deployment + Service  
✔ Jenkins CI/CD (build, push to Minikube, deploy)  
✔ Fully automated pipeline  

---

# 🛠️ Technologies Used
- Python + Flask  
- Docker  
- Kubernetes (Minikube)  
- Jenkins  
- GitHub  
- YAML (K8s manifests)

---

# 📁 Project Structure

```
recipe-app/
│── app.py
│── requirements.txt
│── Dockerfile
│── deployment.yaml
│── service.yaml
│── jenkins-deployment.yaml
│── jenkins-service.yaml
└── README.md
```

---

# ⚙️ Setup Instructions (Step-by-Step)

Follow these exact steps to set up and run the project.

---

## **1️⃣ Install Required Tools**

### Install Docker  
https://www.docker.com/products/docker-desktop/

### Install Minikube  
https://minikube.sigs.k8s.io/docs/start/

### Install kubectl  
```
choco install kubernetes-cli
```

### Install Jenkins (Windows Installer)
https://www.jenkins.io/download/

✔ After installation, access Jenkins at:  
👉 http://localhost:8080  
✔ Enter admin password from:  
```
C:\Program Files\Jenkins\secrets\initialAdminPassword
```

---

## **2️⃣ Clone the Repository**

```
git clone https://github.com/<your-username>/recipe-app.git
cd recipe-app
```

---

## **3️⃣ Start Minikube**

```
minikube start
```

Check status:

```
minikube status
```

---

## **4️⃣ Build Docker Image**

```
docker build -t recipe-app-k8s .
```

---

## **5️⃣ Load Image into Minikube**

```
minikube image load recipe-app-k8s
```

---

## **6️⃣ Apply Kubernetes Files**

```
minikube kubectl -- apply -f deployment.yaml
minikube kubectl -- apply -f service.yaml
```

Check pods:

```
minikube kubectl -- get pods
```

Expose service:

```
minikube service recipe-service
```

---

# 🔧 Jenkins CI/CD Pipeline Setup

### **Create New Pipeline in Jenkins**  
→ *New Item* → *Pipeline*

Paste the following script:

```groovy
pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sowmiya-projects/recipe-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t recipe-app-k8s:latest .'
            }
        }

        stage('Load Image to Minikube') {
            steps {
                bat 'minikube image load recipe-app-k8s:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'minikube kubectl -- apply -f deployment.yaml'
                bat 'minikube kubectl -- apply -f service.yaml'
            }
        }

        stage('Verify Pods') {
            steps {
                bat 'minikube kubectl -- get pods'
            }
        }
    }
}
```

---

# 📦 Dockerfile

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

# 📄 Kubernetes Deployment (deployment.yaml)

```yaml
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
      - name: recipe-container
        image: recipe-app-k8s
        imagePullPolicy: Never
        ports:
        - containerPort: 5000
```

---

# 📄 Kubernetes Service (service.yaml)

```yaml
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
    nodePort: 30010
```

---

# 📄 Jenkins Deployment (jenkins-deployment.yaml)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins
  template:
    metadata:
      labels:
        app: jenkins
    spec:
      containers:
        - name: jenkins-container
          image: jenkins/jenkins:lts
          imagePullPolicy: Never
          ports:
            - containerPort: 8080
            - containerPort: 50000
```

---

# 📄 Jenkins Service (jenkins-service.yaml)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: jenkins-service
spec:
  type: NodePort
  selector:
    app: jenkins
  ports:
    - port: 8080
      targetPort: 8080
      nodePort: 30080
```

---

# 🎉 Result

✔ Fully working DevOps pipeline  
✔ Docker → Minikube → Kubernetes  
✔ Automated Jenkins CI/CD  
✔ Production-like deployment workflow  

---

# 📸 Project Banner

![Project Banner](A_banner_for_a_software_development_project_displa.png)

---

# 🤝 Contributing
Pull requests are welcome!

---

# 📜 License
This project is open-source and free to use.

