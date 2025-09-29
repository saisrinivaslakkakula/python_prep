pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    mkdir -p artifacts
                    python -m exercise_2b --r yes
                '''
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'artifacts/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "✅ Build and tests passed!"
        }
        failure {
            echo "❌ Build failed. Check logs and artifacts."
        }
    }
}
