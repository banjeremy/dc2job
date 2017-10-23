pipeline {
  agent any
  parameters {
    string(name: 'NAMESPACE', defaultValue: 'my-namespace', description: 'What namespace is the DeploymentConfig in?')
    string(name: 'DC_NAME', defaultValue: 'my-deployment-config', description: 'What is the name of the DeploymentConfig?')
  }
  triggers {
    cron('* * * * *')
  }
  stages {
    stage('Run') {
      steps {
        sh "python dc2job.py openshift.default.svc.cluster.local ${cat /var/run/secrets/kubernetes.io/serviceaccount/token} ${params.NAMESPACE} ${params.DC_NAME}"
      }
    }
  }
}
