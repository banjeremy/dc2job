# dc2job
Tool for converting OpenShift `DeploymentConfigs` to `Jobs`. Given a namespace and a dc name, this script will submit a run-once job that executes to completion. 

## Environment Variables
Before invoking the tool, make sure you set the following environment variables:
```
OPENSHIFT_HOST=<your openshift url and port>
TOKEN=<your openshift api token>
```

## Usage
```
./dc2job <namespace> <deployment_config_name>
```

### Example
```
OPENSHIFT_HOST=https://openshift.redhat.com:8443 \
TOKEN=$(oc whoami -t) \
./dc2job my-project my-deployment-config
```
