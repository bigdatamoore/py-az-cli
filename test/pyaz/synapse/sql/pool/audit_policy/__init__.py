import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(resource_group, workspace_name, name):
    params = get_params(locals())   
    command = "az synapse sql pool audit-policy show " + params
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

def update(resource_group, workspace_name, name, state=None, storage_account=None, storage_endpoint=None, storage_key=None, storage_subscription=None, use_secondary_key=None, retention_days=None, actions=None, enable_azure_monitor=None, blob_auditing_policy_name=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az synapse sql pool audit-policy update " + params
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
