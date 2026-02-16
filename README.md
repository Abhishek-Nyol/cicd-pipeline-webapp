\# CI/CD Pipeline for Web Application using Docker, Kubernetes \& GitHub Actions



\## Project Overview



This project demonstrates a complete CI/CD pipeline for a Python web application using:



\* Docker for containerization

\* Kubernetes for container orchestration

\* GitHub Actions for automation

\* Docker Hub for image storage



The pipeline automatically builds and pushes the Docker image and deploys the application.



---



\## Application Features



\* Simple Python Web Application

\* Displays project information

\* Shows container hostname

\* Shows running status

\* Shows timestamp



---



\## Tech Stack



\* Python

\* Docker

\* Kubernetes

\* GitHub Actions

\* Docker Hub



---



\## Project Structure



```

cicd-pipeline-webapp

│

├── app.py

├── Dockerfile

├── requirements.txt

├── README.md

│

├── k8s

│   ├── deployment.yaml

│   └── service.yaml

│

└── .github

&nbsp;   └── workflows

&nbsp;       └── main.yml

```



---



\## Docker Image



Docker Hub Repository:



```

https://hub.docker.com/r/abhisheknyol704/cicd-webapp

```



---



\## Kubernetes Deployment



Deployment File:



```

k8s/deployment.yaml

```



Service File:



```

k8s/service.yaml

```



---



\## CI/CD Pipeline Workflow



GitHub Actions automatically performs:



\* Build Docker Image

\* Push to Docker Hub



Workflow file location:



```

.github/workflows/main.yml

```



---



\## How to Run the Project



\### Step 1: Clone Repository



```

git clone https://github.com/YOUR\_USERNAME/cicd-pipeline-webapp.git

```



---



\### Step 2: Build Docker Image



```

docker build -t cicd-webapp .

```



---



\### Step 3: Run Container



```

docker run -p 5000:5000 cicd-webapp

```



Open in browser:



```

http://localhost:5000

```



---



\### Step 4: Deploy to Kubernetes



Apply deployment:



```

kubectl apply -f k8s/deployment.yaml

```



Apply service:



```

kubectl apply -f k8s/service.yaml

```



---



\## Output



Application runs successfully showing:



\* Project Name

\* Status

\* Version

\* Time

\* Hostname



---



---



\## Purpose of Project



This project was created to demonstrate practical implementation of:



\* CI/CD Pipeline

\* Docker

\* Kubernetes

\* GitHub Actions



for DevOps learning and professional portfolio.



---



