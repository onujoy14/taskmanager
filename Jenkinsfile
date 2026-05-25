pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ -v --break-system-packages || python -m pytest tests/ -v'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "App is already running via docker compose"'
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
