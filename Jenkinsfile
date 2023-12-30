pipeline {
    agent any 
    tools {
        jdk 'jdk-17'
    }
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }
    stages{
        stage("clean workspace") {
            steps {
                cleanWs()
            }
        }
        stage("GithubCode"){
            steps {
                echo "Cloning the code"
                git url:"https://github.com/SB321/Gym-Workout-Tracker.git", branch: "master"
            }
        }
        stage("Sonarqube Analysis") {
            steps {
                withSonarQubeEnv('Sonar-server') {
                    sh '''$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=Gym-App \
                    -Dsonar.projectKey=Gym-App'''
                }
            }
        }
        stage("quality gate") {
            steps {
                sleep(60)
                timeout(time: 1, unit: 'MINUTES') {
                    
                    script{
                        
                        def qg = waitForQualityGate()
                        print "Finished waiting"
                        if (qg.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        }
                    }
                    
                }  
            }
        }
        stage("Build"){
            steps {
                echo "Building the image"
                sh "docker build -t gymsprint-app ."
                
            }
        }
        
        stage("Push to Docker Hub"){
            steps {
                echo "Pushing the image to Docker Hub"
                withCredentials([usernamePassword(credentialsId:"DockerHub",passwordVariable:"DockerHubPass",usernameVariable:"DockerHubUser")]){
                    sh "docker tag gymsprint-app ${env.DockerHubUser}/gymsprint-app:latest"
                    withDockerRegistry([ credentialsId: "DockerHub", url: "" ]) {
                    
                        sh "docker push ${env.DockerHubUser}/gymsprint-app:latest"
         
                    }
                
                }
            }
        }
        
        stage("Run"){
            
            steps{
                
                echo "Scheduled to Run Docker image"
                withCredentials([usernamePassword(credentialsId:"DockerHub",passwordVariable:"DockerHubPass",usernameVariable:"DockerHubUser")]){
                
                    withDockerRegistry([ credentialsId: "DockerHub", url: "" ]) {
                    
                        sh "docker run -d --name gymsprint-app -p 8000:8000 ${env.DockerHubUser}/gymsprint-app:latest"
         
                    }
                
                }
                
            }
        }

    }
}
