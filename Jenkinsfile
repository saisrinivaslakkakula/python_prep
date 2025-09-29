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
                    echo "Running system tests..."

                    # Test 1: addition
                    output=$(/usr/local/bin/docker run --rm $IMAGE_NAME:${BUILD_NUMBER} 1 + 2)
                    [ "$output" = "3" ] || { echo "FAIL: expected 3, got $output"; exit 1; }

                    # Test 2: subtraction
                    output=$(/usr/local/bin/docker run --rm $IMAGE_NAME:${BUILD_NUMBER}  1 - 2)
                    [ "$output" = "-1" ] || { echo "FAIL: expected -1, got $output"; exit 1; }

                    echo "✅ All system tests passed!"
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
