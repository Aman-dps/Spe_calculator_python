# International Institute of Information Technology, Bangalore
## Software Production Engineering Mini Project Report
### Scientific Calculator

Submitted by  
Aman Tiwari  
MT2025018 

In the guidance of Prof. B. Thangaraju

**GitHub Repository:**  
[https://github.com/Aman-dps/Spe_calculator_python](https://github.com/Aman-dps/Spe_calculator_python)  

**DockerHub Repository:**  
[https://hub.docker.com/repositories/atrocks](https://hub.docker.com/repositories/atrocks)  

---

## Table of Contents
1. Abstract
2. DevOps
3. Tools and Technologies Used
4. Source Code Management
5. Docker
6. Jenkins
7. Ansible
8. Source Code
9. Adding Test Cases
10. Webhooks & Email Notification
11. Conclusion

---

## 1. Abstract
The Scientific Calculator project is a software application developed to perform various mathematical and scientific operations such as factorial, square root, logarithmic calculations, and power computations on user-provided numbers. The primary goal of this project is to implement a simple yet functional scientific calculator while integrating modern DevOps practices to improve the software development and deployment process.

DevOps techniques are incorporated in this project to automate and streamline the stages of development, testing, and deployment. The application is developed using modern software development methodologies and includes automated testing to ensure the accuracy and reliability of the implemented mathematical operations.

The project utilizes a Continuous Integration and Continuous Deployment (CI/CD) pipeline to automate the build and deployment workflow. Several DevOps tools are used in the pipeline, including GitHub for version control, Python `venv` & `pip` for package management, Jenkins for continuous integration, Docker for containerization, and Ansible for automated deployment. By integrating these DevOps tools and practices, the project demonstrates how automation can improve software reliability, scalability, and maintainability.

## 2. DevOps
### What is DevOps?
DevOps is a software development methodology that integrates the Development (Dev) and Operations (Ops) teams to collaborate throughout the entire lifecycle of an application. The primary goal of DevOps is to improve collaboration, automate processes, and accelerate the delivery of applications and services.

Traditionally, development and operations teams worked separately, which often caused delays in software delivery and deployment. DevOps addresses this issue by promoting Continuous Integration (CI), Continuous Testing, and Continuous Deployment (CD), allowing teams to deliver software updates more efficiently and reliably.

### Advantages of DevOps
DevOps provides several benefits:
1. **Faster Delivery:** Automates build, testing, and deployment processes.
2. **Improved Software Quality:** Continuous integration and automated testing help detect errors early.
3. **Better Collaboration:** Reduces communication barriers between Dev and Ops teams.
4. **Enhanced Security:** Vulnerabilities can be detected earlier in the cycle.
5. **Scalability and Reliability:** Containerization allows applications to scale efficiently.

## 3. Tools and Technologies Used

- **Programming Language – Python 3.9**
  The scientific calculator application is developed using Python. It implements mathematical operations such as square root, factorial, natural logarithm, and power calculations.
- **Version Control – Git and GitHub**
  Git is used to manage the version control of the project source code. GitHub acts as a remote repository for code storage, collaboration, and version management.
- **Dependency Management – pip and venv**
  Python's built-in `venv` is used to create virtual environments, and `pip` is used as the package installer to manage project dependencies like `pytest`.
- **Testing Framework – pytest**
  `pytest` is used to test the functionality of the calculator operations. It ensures that the implemented mathematical functions work correctly and helps detect errors during development.
- **Continuous Integration – Jenkins**
  Jenkins is used to implement the CI/CD pipeline. It automatically triggers the build process when code changes are pushed to GitHub, runs tests, builds the Docker image, and prepares it for deployment.
- **Containerization – Docker**
  Docker is used to containerize the application along with all its dependencies, ensuring that the application runs consistently across different environments.
- **Container Registry – DockerHub**
  DockerHub is used to store the Docker images created during the pipeline process. These images can be pulled and deployed on different systems.
- **Deployment Automation – Ansible**
  Ansible is used for automating the deployment of the Docker container. It pulls the Docker image from DockerHub and runs the container on the target machine.
- **Webhook Tunnelling – ngrok** *(Optional/As per original project)*
  `ngrok` is used to expose the local Jenkins server to the internet, enabling GitHub webhooks to trigger the Jenkins pipeline automatically.

## 4. Source Code Management
Source Code Management (SCM) is used to track and manage changes made to the source code of a project. It helps developers maintain version history and collaborate efficiently.
In this project, Git is used as the version control system and GitHub is used as the remote repository to store the project code.

Common Git commands used:
```bash
git init
git status
git add .
git commit -m "Initial Commit"
git remote add origin https://github.com/Aman-dps/Spe_calculator_python.git
git push -u origin main
```

*(Insert GitHub Repository Screenshot Here)*

## 5. Docker
Docker is a containerization platform used to package an application along with its dependencies so that it can run consistently across different environments. In this project, Docker is used to containerize the Python Scientific Calculator application.

A Docker image is created using the following `Dockerfile`.

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY calculator.py /app/calculator.py

CMD ["python", "calculator.py"]
```

The following commands can be used to manually build and run the Docker image:
```bash
docker build -t scientific-calculator .
docker tag scientific-calculator atrocks/scientific-calculator:latest
docker push atrocks/scientific-calculator:latest
docker run -it atrocks/scientific-calculator:latest
```

*(Insert DockerHub Screenshot Here)*

## 6. Jenkins
Jenkins is an open-source automation tool used for Continuous Integration (CI) and Continuous Delivery (CD).
Whenever a new commit is pushed to the GitHub repository, the Jenkins pipeline is automatically triggered (e.g., via a webhook).

The major steps performed in the pipeline are:
1. **Clone Git:** Pull the latest source code from the GitHub repository (`main` branch).
2. **Install Dependencies:** Set up a Python virtual environment and install `pytest`.
3. **Test the Project:** Run tests using `pytest test_calculator.py`.
4. **Build Docker Image:** Build the container image.
5. **Push Docker Image:** Authenticate and push the image to DockerHub (`atrocks/scientific-calculator`).
6. **Deploy with Ansible:** Run the Ansible playbook to deploy the updated container.

**Jenkinsfile:**
```groovy
pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'scientific-calculator'
        GITHUB_REPO_URL = 'https://github.com/Aman-dps/Spe_calculator_python.git'
        DOCKER_HUB_USERNAME = 'atrocks'
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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install pytest
                '''
            }
        }

        stage('Test the Project') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest test_calculator.py
                '''
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
                    sh "docker build -t ${DOCKER_IMAGE_NAME} ."
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credential', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo \\$DOCKER_PASS | docker login -u \\$DOCKER_USER --password-stdin"
                        sh "docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                        sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    sh 'ansible-playbook -i inventory deploy.yml'
                }
            }
        }
    }
}
```

*(Insert Jenkins Configuration and Pipeline Screenshots Here)*

## 7. Ansible
Ansible is used for automating the deployment process in the CI/CD pipeline. The deployment steps are written in a YAML file called a playbook (`deploy.yml`).

The Jenkins pipeline executes this Ansible playbook to pull the Docker image from DockerHub, stop any running obsolete container, and run the new container.

**deploy.yml:**
```yaml
---
- name: Deploy Scientific Calculator Docker Container
  hosts: all
  become: no
  tasks:
    - name: Pull the latest Docker Hub image
      community.docker.docker_image:
        name: "{{ lookup('env', 'DOCKER_HUB_USERNAME') }}/scientific-calculator"
        tag: latest
        source: pull

    - name: Stop and remove any existing calculator container
      community.docker.docker_container:
        name: scientific-calculator-app
        state: absent

    - name: Run the newly built container
      community.docker.docker_container:
        name: scientific-calculator-app
        image: "{{ lookup('env', 'DOCKER_HUB_USERNAME') }}/scientific-calculator:latest"
        state: started
        restart_policy: unless-stopped
        interactive: yes
        tty: yes
```

**inventory:**
```ini
[local]
localhost ansible_connection=local
```

*(Insert Ansible Execution Screenshot Here)*

## 8. Source Code
The following section contains the source code of the Scientific Calculator application developed in Python. The program implements basic scientific operations such as square root, factorial, logarithm, and power calculations.

**calculator.py:**
```python
import math

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Error! Division by zero.")
        return a / b

    @staticmethod
    def power(base, exponent):
        return math.pow(base, exponent)

    @staticmethod
    def square_root(num):
        if num < 0:
            raise ValueError("Error! Square root of a negative number.")
        return math.sqrt(num)

    @staticmethod
    def logarithm(num):
        if num <= 0:
            raise ValueError("Error! Logarithm of zero or negative number.")
        return math.log(num)

    @staticmethod
    def factorial(num):
        if num < 0:
            raise ValueError("Error! Factorial of a negative number.")
        if not float(num).is_integer():
             raise ValueError("Error! Factorial of non-integer.")
        return float(math.factorial(int(num)))

if __name__ == "__main__":
    while True:
        print("Scientific Calculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        print("5. Power\n6. Square Root\n7. Logarithm\n8. Factorial")
        print("9. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 9:
            print("Exiting the calculator...")
            break

        try:
            if choice in [1, 2, 3, 4, 5]:
                if choice == 5:
                     print("Enter base and exponent: ")
                else:
                     print("Enter two numbers: ")
                
                num1 = float(input())
                num2 = float(input())

                if choice == 1:
                    print(f"Result: {Calculator.add(num1, num2)}")
                elif choice == 2:
                    print(f"Result: {Calculator.subtract(num1, num2)}")
                elif choice == 3:
                    print(f"Result: {Calculator.multiply(num1, num2)}")
                elif choice == 4:
                    print(f"Result: {Calculator.divide(num1, num2)}")
                elif choice == 5:
                    print(f"Result: {Calculator.power(num1, num2)}")

            elif choice in [6, 7, 8]:
                print("Enter a number: ")
                num1 = float(input())

                if choice == 6:
                    print(f"Result: {Calculator.square_root(num1)}")
                elif choice == 7:
                    print(f"Result: {Calculator.logarithm(num1)}")
                elif choice == 8:
                    print(f"Result: {Calculator.factorial(num1)}")
            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(e)
        except Exception as e:
             print(f"An error occurred: {e}")
```

## 9. Adding Test Cases
Unit Testing is the process of testing individual components of a program to ensure that each part works correctly. A unit represents the smallest testable part of an application, such as a method, function, or class.

In this project, `pytest` is used to implement unit tests for the scientific calculator operations such as factorial, square root, logarithm, and power functions.

**test_calculator.py:**
```python
import pytest
import math
from calculator import Calculator

class TestCalculator:

    def test_add(self):
        assert Calculator.add(6, 5) == 11.0
        assert Calculator.add(-2, 1) == -1.0
        assert Calculator.add(0, 0) == 0.0

    def test_subtract(self):
        assert Calculator.subtract(3, 2) == 1.0
        assert Calculator.subtract(-2, 1) == -3.0
        assert Calculator.subtract(0, 0) == 0.0

    def test_multiply(self):
        assert Calculator.multiply(2, 3) == 6.0
        assert Calculator.multiply(-2, 1) == -2.0
        assert Calculator.multiply(0, 3) == 0.0

    def test_divide(self):
        assert Calculator.divide(6, 3) == 2.0
        assert Calculator.divide(-6, 3) == -2.0
        with pytest.raises(ValueError, match="Error! Division by zero."):
            Calculator.divide(1, 0)

    def test_power(self):
        assert Calculator.power(2, 3) == 8.0
        assert Calculator.power(2, 0) == 1.0
        assert Calculator.power(2, -2) == 0.25

    def test_square_root(self):
        assert Calculator.square_root(16) == 4.0
        assert Calculator.square_root(0) == 0.0
        with pytest.raises(ValueError, match="Error! Square root of a negative number."):
            Calculator.square_root(-1)

    def test_logarithm(self):
        assert math.isclose(Calculator.logarithm(2), math.log(2), rel_tol=1e-9)
        assert Calculator.logarithm(1) == 0.0
        with pytest.raises(ValueError, match="Error! Logarithm of zero or negative number."):
            Calculator.logarithm(0)
        with pytest.raises(ValueError, match="Error! Logarithm of zero or negative number."):
            Calculator.logarithm(-1)

    def test_factorial(self):
        assert Calculator.factorial(5) == 120.0
        assert Calculator.factorial(0) == 1.0
        assert Calculator.factorial(1) == 1.0
        with pytest.raises(ValueError, match="Error! Factorial of a negative number."):
            Calculator.factorial(-5)
```

*(Insert Pytest Execution Screenshot Here)*

## 10. Webhooks & Email Notification

### Webhooks
Webhooks are automated HTTP callbacks that trigger actions when an event occurs, such as a code push in a repository. Tools like **Ngrok** can be used to expose Jenkins running on a local machine to the internet, enabling webhooks to communicate with it.

*(Insert Webhook Configuration Screenshot Here)*

### Email Notification
SMTP (Simple Mail Transfer Protocol) allows Jenkins to send email notifications about build status, failures, or successes to developers. This ensures timely updates on project progress.

*(Insert Email Sent By Jenkins Screenshot Here)*

## 11. Conclusion
The Scientific Calculator project demonstrates the implementation of a simple application integrated with modern DevOps practices. The application performs scientific calculations such as factorial, square root, logarithm, and power operations using Python.

The project successfully implements a CI/CD pipeline using tools such as GitHub, Jenkins, Docker, DockerHub, and Ansible. The pipeline automates the process of building the application, running unit tests, creating Docker images, pushing images to DockerHub, and deploying the application using Ansible.

By using DevOps tools and automation techniques, the project improves the efficiency, reliability, and consistency of the software development and deployment process.

**GitHub Repository:**  
[https://github.com/Aman-dps/Spe_calculator_python](https://github.com/Aman-dps/Spe_calculator_python)  

**DockerHub Repository:**  
[https://hub.docker.com/repositories/atrocks](https://hub.docker.com/repositories/atrocks)
