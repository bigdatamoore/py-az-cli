import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(all=None, management_group=None, resource_group=None, resource=None, namespace=None, parent=None, resource_type=None, policy_set_definition=None, policy_definition=None, policy_assignment=None, from_=None, to=None, order_by=None, select=None, top=None, filter=None, apply=None, expand=None):
    params = get_params(locals())   
    command = "az policy state list " + params
    print(command)
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        return json.loads(stdout)
        print(stdout)
    else:
        raise Exception(stderr)
        print(stderr)  

def summarize(management_group=None, resource_group=None, resource=None, namespace=None, parent=None, resource_type=None, policy_set_definition=None, policy_definition=None, policy_assignment=None, from_=None, to=None, top=None, filter=None):
    params = get_params(locals())   
    command = "az policy state summarize " + params
    print(command)
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        return json.loads(stdout)
        print(stdout)
    else:
        raise Exception(stderr)
        print(stderr)  

def trigger_scan(resource_group=None, no_wait=None):
    params = get_params(locals())   
    command = "az policy state trigger-scan " + params
    print(command)
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        return json.loads(stdout)
        print(stdout)
    else:
        raise Exception(stderr)
        print(stderr)  
