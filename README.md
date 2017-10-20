# dc2job
Tools for converting OpenShift `DeploymentConfig`s to `Job`s

## Environment Variables
The tools expects the following environment variables to be set.
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
