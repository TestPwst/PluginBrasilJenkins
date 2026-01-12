pipeline {
    agent any

    environment {
        VENV = ".venv"
        PYTHONUNBUFFERED = "1"
        SONARQUBE_ENV = "SonarQubePluginBrasil"
        DEPENDENCY_CHECK_DIR = "dependency-check"
        // Asegúrate de que el ID 'snyk-token' esté creado en Jenkins -> Credentials
        SNYK_TOKEN = credentials('Token_Snyk')
    }

    stages {
        // Quitamos el stage de Git manual porque SCM lo hace por ti

        stage('Initialize & Version') {
            steps {
                bat 'python --version'
                // Creamos la carpeta de logs si no existe para que los tests no fallen
                bat 'if not exist logs mkdir logs'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                python -m venv %VENV%
                call %VENV%\\Scripts\\activate.bat
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Snyk Scan') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat """
                    npm install -g snyk
                    snyk auth %SNYK_TOKEN%
                    snyk test --all-projects
                    """
                }
            }
        }

        stage('OWASP Dependency-Check') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat """
                    if not exist %DEPENDENCY_CHECK_DIR% (
                        curl -L -o dc.zip https://github.com/jeremylong/DependencyCheck/releases/latest/download/dependency-check.zip
                        tar -xf dc.zip
                    )

                    %DEPENDENCY_CHECK_DIR%\\bin\\dependency-check.bat ^
                        --scan . ^
                        --format HTML ^
                        --out dependency-check-report ^
                        --disableAssembly
                    """
                }
            }
        }

        /* ===================== SONARQUBE ===================== */
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    bat """
                    sonar-scanner ^
                      -Dsonar.projectKey=SonarQubePluginBrasil ^
                      -Dsonar.sources=. ^
                      -Dsonar.language=py ^
                      -Dsonar.python.version=3 ^
                      -Dsonar.sourceEncoding=UTF-8
                    """
                }
            }
        }

        /* ===================== PRUEBAS FLUJOS ===================== */

        stage('FLJ01') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat """
                    call %VENV%\\Scripts\\activate.bat
                    set PYTHONPATH=%WORKSPACE%
                    pytest Brasil\\FLUJOS\\FLJ01.py -s -o log_cli=true > logs\\FLJ01.log 2>&1
                    """
                }
            }
        }

        stage('FLJ02') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat """
                    call %VENV%\\Scripts\\activate.bat
                    set PYTHONPATH=%WORKSPACE%
                    pytest Brasil\\FLUJOS\\FLJ02.py -s -o log_cli=true > logs\\FLJ02.log 2>&1
                    """
                }
            }
        }

        stage('FLJ04') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat """
                    call %VENV%\\Scripts\\activate.bat
                    set PYTHONPATH=%WORKSPACE%
                    pytest Brasil\\FLUJOS\\FLJ04.py -s -o log_cli=true > logs\\FLJ04.log 2>&1
                    """
                }
            }
        }
        stage('Run Automation (HTML Report)') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat """
                    call %VENV%\\Scripts\\activate.bat
                    set PYTHONPATH=%WORKSPACE%
                    python Run_test.py
                    """
                }
            }
        }
    }

    post {
        always {

            script {
                publishHTML(target: [
                    reportDir: 'results',
                    reportFiles: '**/*.html',
                    reportName: 'Reporte Automatización (HTML)',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: true
                ])
            }
        }

        failure {
            emailext(
                subject: "❌ FALLÓ Pipeline PluginBrasil - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                to: "testingmexico1@gmail.com",
                body: """
    Hola equipo,

    ❌ El pipeline PluginBrasil FALLÓ.

    Job: ${env.JOB_NAME}
    Build: ${env.BUILD_NUMBER}
    URL: ${env.BUILD_URL}

    📄 Revisar reportes HTML generados automáticamente:
    - Reportes por test (con imágenes)
    - Logs en results/**/logs/execution.log

    Saludos,
    Jenkins 🤖
    """
            )
        }
    }
}
