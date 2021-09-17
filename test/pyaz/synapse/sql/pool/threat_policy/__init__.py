import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(resource_group, workspace_name, name, security_alert_policy_name):
    params = get_params(locals())   
    command = "az synapse sql pool threat-policy show " + params
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

def update(resource_group, workspace_name, name, security_alert_policy_name=None, state=None, storage_account=None, storage_endpoint=None, storage_key=None, retention_days=None, email_addresses=None, disabled_alerts=None, email_account_admins=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az synapse sql pool threat-policy update " + params
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
