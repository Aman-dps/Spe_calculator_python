pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'scientific-calculator'
        GITHUB_REPO_URL = 'https://github.com/Aman-dps/Spe_calculator_python.git'
        DOCKER_HUB_USERNAME = 'atrocks'
        // Docker Desktop maps its executable here. This explicitly adds it to Jenkins PATH.
        PATH = "/Applications/Docker.app/Contents/Resources/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
    }

    stages {
        stage('Clone Git') {
            steps {
                script {
                    git branch: 'main',
                        url: "${GITHUB_REPO_URL}"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install pytest'
            }
        }

        stage('Test the Project') {
            steps {
                sh 'python3 -m pytest test_calculator.py'
            }
        }

        stage('Debug Docker') {
            steps {
                sh 'echo PATH=$PATH'
                sh 'which docker || true'
                sh 'ls -l /usr/local/bin/docker || true'
                sh 'docker --version || true'
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
}
