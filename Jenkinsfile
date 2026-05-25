pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/ -v'
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
