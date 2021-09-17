import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, vault_name, name, server_name, protectable_item_type, workload_type):
    params = get_params(locals())   
    command = "az backup protectable-item show " + params
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

def list(resource_group, vault_name, workload_type, backup_management_type=None, container_name=None, protectable_item_type=None, server_name=None):
    params = get_params(locals())   
    command = "az backup protectable-item list " + params
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

def initialize(resource_group, vault_name, container_name, workload_type):
    params = get_params(locals())   
    command = "az backup protectable-item initialize " + params
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
