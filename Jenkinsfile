pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-u287ur', url: 'https://github.com/u287ur/flask-app.git'
            }
        }
        
        stage('Build & Push Image') {
            steps {
                withCredentials([
                usernamePassword(credentialsId: 'dockerhub-u287ur', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')
                ]) {
                    script {
                        def tag = new Date().format('yyyyMMdd-HHmm')
                        sh """
                            docker logout || true
                            docker login -u "$DOCKERHUB_USERNAME" -p "$DOCKERHUB_PASSWORD"

                            docker build -t "$DOCKERHUB_USERNAME/github-actions:latest" .
                            docker tag $DOCKERHUB_USERNAME/github-actions:latest $DOCKERHUB_USERNAME/github-actions:${tag}

                            docker push $DOCKERHUB_USERNAME/github-actions:latest
                            docker push $DOCKERHUB_USERNAME/github-actions:${tag}
                        """
                    }
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

    post {
        success {
            echo "✅ Deployment completed successfully."
        }
        failure {
            echo "❌ Deployment failed!"
        }
    }
}