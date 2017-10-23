pipeline {
    agent any
    parameters {
      string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    }
    triggers {
        cron('* * * * *')
    }
    stages {
        stage('Run') {
            steps {
                echo "python dc2job.py ${params.NAMESPACE} ${params.DC_NAME}"
            }
        }
    }
}
