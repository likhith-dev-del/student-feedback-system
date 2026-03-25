pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git '<your-repo-url>'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t feedback-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop feedback-app || true'
                sh 'docker rm feedback-app || true'
                sh 'docker run -d -p 5000:5000 --name feedback-app feedback-app'
            }
        }

        stage('Ansible Deploy') {
            steps {
                sh 'ansible-playbook ansible/deploy.yml'
            }
        }
    }
}