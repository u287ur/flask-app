pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = credentials('dockerhub-username')
        DOCKERHUB_PASSWORD = credentials('dockerhub-password')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def tag = new Date().format('yyyyMMdd-HHmm')
                    sh """
                        docker build -t $DOCKERHUB_USERNAME/github-actions:latest .
                        docker tag $DOCKERHUB_USERNAME/github-actions:latest $DOCKERHUB_USERNAME/github-actions:${tag}
                    """
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    sh """
                        echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin
                        docker push $DOCKERHUB_USERNAME/github-actions:latest
                        docker push $DOCKERHUB_USERNAME/github-actions:\$(date +'%Y%m%d-%H%M')
                    """
                }
            }
        }
        stage('Deploy with Docker Compose') {
            steps {
                sh """
                    docker compose pull
                    docker compose up -d
                """
            }
        }
    }
}