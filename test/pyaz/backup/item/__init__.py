import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, vault_name, container_name, name, backup_management_type=None, workload_type=None, use_secondary_region=None):
    params = get_params(locals())   
    command = "az backup item show " + params
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

def list(resource_group, vault_name, workload_type=None, container_name=None, backup_management_type=None, use_secondary_region=None):
    params = get_params(locals())   
    command = "az backup item list " + params
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

def set_policy(resource_group, vault_name, container_name, name, policy_name, workload_type=None, backup_management_type=None):
    params = get_params(locals())   
    command = "az backup item set-policy " + params
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
