pipeline {
    agent any

    environment {
        IMAGE_NAME = "calc-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python & Run Unit Tests') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                    pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t calc-app:${BUILD_NUMBER} .'
            }
        }

        stage('System Tests') {
            steps {
                sh '''
                chmod +x system_tests.sh
                ./system_tests.sh calc-app:${BUILD_NUMBER}
                '''
            }
        }

        stage('Archive Results') {
            steps {
                sh '''
                    mkdir -p artifacts
                    echo "Build: ${BUILD_NUMBER}" > artifacts/build_info.txt
                    echo "System tests passed." > artifacts/system_test_results.txt
                '''
                archiveArtifacts artifacts: 'artifacts/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "✅ Build + Unit Tests + System Tests passed!"
        }
        failure {
            echo "❌ Build failed. Check logs & artifacts."
        }
    }
}
