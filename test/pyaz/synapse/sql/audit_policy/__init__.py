import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_group, workspace_name, blob_auditing_policy_name):
    params = get_params(locals())   
    command = "az synapse sql audit-policy show " + params
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

def update(resource_group, workspace_name, blob_auditing_policy_name=None, state=None, storage_account=None, storage_endpoint=None, storage_key=None, retention_days=None, actions=None, storage_subscription=None, use_secondary_key=None, enable_azure_monitor=None, queue_delay_time=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az synapse sql audit-policy update " + params
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

def wait(resource_group, workspace_name, blob_auditing_policy_name, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az synapse sql audit-policy wait " + params
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
