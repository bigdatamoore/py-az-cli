import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(server, resource_group, name):
    params = get_params(locals())   
    command = "az sql db audit-policy show " + params
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

def update(resource_group, server, name, state=None, blob_storage_target_state=None, storage_account=None, storage_endpoint=None, storage_key=None, actions=None, retention_days=None, log_analytics_target_state=None, log_analytics_workspace_resource_id=None, event_hub_target_state=None, event_hub_authorization_rule_id=None, event_hub=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az sql db audit-policy update " + params
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

def wait(resource_group, server, name, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az sql db audit-policy wait " + params
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
