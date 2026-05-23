pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ganesh939259-dotcom/employee-management.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r employee-management-devops/requirements.txt'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-management employee-management-devops/'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker-compose -f employee-management-devops/docker-compose.yml up -d'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
