pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '--entrypoint=""'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ -v'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Tests passed - app is deployed"'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! All tests passed.'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
