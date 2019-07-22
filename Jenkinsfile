pipeline {
    agent {
	docker {image 'begun74/my_flask:v1.1'}
    }
    environment {
    }
    stages {
        stage('Example stage 1') {
            steps {
                sh 'docker build -f "Dockerfile" -t begun74/my_flask::latest .' 
            }
        }
        stage('Example stage 2') {
            steps {
                sh 'docker push begun74/my_flask::latest'
            }
        }
    }
}
