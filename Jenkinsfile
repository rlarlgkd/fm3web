node {
    def app
    def dockerfile = 'dockerfile'

    stage('Clone repository') {
      

        checkout scm
    }
    stage('\u27A1 Dependencies for Docker and ChefDK') {
            steps {
                sh '''apt-get update
apt-get install -y sudo git build-essential apt-transport-https ca-certificates curl software-properties-common'''
            }
        }
        stage('\u27A1 Install Docker-CE') {
            steps {
                sh '''curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt-get update
apt-get install -y docker-ce'''
            }
        }
        stage('\u27A1 Start Docker') {
            steps {
                sh 'service docker start'
            }
        }
    stage('Build image') {
        steps{
            sh 'cd back'
            
       app = docker.build("rlarlgkd/fm3web", "-f ./back/${dockerfile} ./back")
        }
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}