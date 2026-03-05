pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'scientific-calculator'
        GITHUB_REPO_URL = 'https://github.com/Aman-dps/Spe_calculator_python.git'
        DOCKER_HUB_USERNAME = 'atrocks'
        // Allow Jenkins to find brew installations like 'docker' and 'python3' on Mac
        PATH = "/opt/homebrew/bin:/usr/local/bin:$PATH"
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
                // Create a virtual environment and use it to install pytest securely
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install pytest
                '''
            }
        }

        stage('Test the Project') {
            steps {
                // Activate the virtual environment from the previous step and run the tests
                sh '''
                    . venv/bin/activate
                    pytest test_calculator.py
                '''
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
