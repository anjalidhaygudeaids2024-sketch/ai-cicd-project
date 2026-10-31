pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Project checkout successful'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train AI Model') {
            steps {
                sh 'python train_model.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t ai-model:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}