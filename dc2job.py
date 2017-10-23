#!/usr/bin/env python3

import json
import random
import requests
import string
import sys

req_headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


def gen_rand_str(n):
    return '' \
        .join(random.choices(string.ascii_uppercase + string.digits, k=n)) \
        .lower()


def load_job_template():
    with open('job_template.json', 'r') as job_template_file:
        job_template = json.loads(job_template_file)
    return job_template


def get_deploy_config(namespace, name):
    endpoint = "/oapi/v1/namespaces/%(namespace)s/deploymentconfigs/%(name)s" % locals()

    res = requests.get(
        host + endpoint,
        headers=req_headers,
        verify=False
    )

    deploy_config = json.loads(res.text)
    return deploy_config


def dc_to_job(dc, job_template):
    unique_str = gen_rand_str(8)

    for container in dc['spec']['template']['spec']['containers']:
        container['name'] = container['name'] + '-' + unique_str

    job_template['metadata'] = {
        'labels': dc['metadata']['labels'],
        'name': dc['metadata']['name'] + '-' + unique_str,
        'namespace': dc['metadata']['namespace']
    }
    job_template['spec']['template']['metadata'] = {
        'labels': dc['spec']['template']['metadata']['labels']
    }
    job_template['spec']['template']['spec'] = dc['spec']['template']['spec']
    job_template['spec']['template']['spec']['restartPolicy'] = 'Never'

    return job_template


def submit_job(namespace, job):
    endpoint = "/apis/batch/v1/namespaces/%(namespace)s/jobs" % locals()

    res = requests.post(
        host + endpoint,
        headers=req_headers,
        data=json.dumps(job),
        verify=False,
        cert="/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
    )

    return res.text


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("usage:\tpython submit_job.py <host> <token> <namespace> <name>\n")
    else:
        host = sys.argv[1]
        token = sys.argv[2]
        namespace = sys.argv[3]
        name = sys.argv[4]

        job_template = load_job_template()
        dc = get_deploy_config(namespace, name)
        job = dc_to_job(dc, job_template)
        res = submit_job(namespace, job)

        print(res)
