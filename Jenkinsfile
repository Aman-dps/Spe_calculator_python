pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'scientific-calculator'
        GITHUB_REPO_URL = 'https://github.com/Aman-dps/Spe_calculator_python.git'
        DOCKER_HUB_USERNAME = 'atrocks'
    }

    stages {
        stage('Clone Git') {
            steps {
                script {
                    git branch: 'master',
                        url: "${GITHUB_REPO_URL}"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest'
            }
        }

        stage('Test the Project') {
            steps {
                sh 'pytest test_calculator.py'
            }
        }
	
	stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }
	stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'docker-hub-credential') {
                        sh "docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                        sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }

        
}
