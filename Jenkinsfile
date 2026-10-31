pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Project checkout successful'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/python -m pip install --upgrade pip'
                sh 'venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Train AI Model') {
            steps {
                sh 'venv/bin/python train_model.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'venv/bin/python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-model:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}