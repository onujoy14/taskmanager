pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'docker run --rm -v $(pwd):/app -w /app python:3.11-slim pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm -v $(pwd):/app -w /app python:3.11-slim sh -c "pip install -r requirements.txt && pytest tests/ -v"'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded. App is deployed.'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
