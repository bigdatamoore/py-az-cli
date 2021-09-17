import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(vm_resource_id, workspace_id, server_name, database_name, rule_id, vm_name=None, agent_id=None, vm_uuid=None):
    params = get_params(locals())   
    command = "az security va sql baseline show " + params
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

def list(vm_resource_id, workspace_id, server_name, database_name, vm_name=None, agent_id=None, vm_uuid=None):
    params = get_params(locals())   
    command = "az security va sql baseline list " + params
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

def delete(vm_resource_id, workspace_id, server_name, database_name, rule_id, vm_name=None, agent_id=None, vm_uuid=None):
    params = get_params(locals())   
    command = "az security va sql baseline delete " + params
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

def update(vm_resource_id, workspace_id, server_name, database_name, rule_id, baseline=None, latest=None, vm_name=None, agent_id=None, vm_uuid=None):
    params = get_params(locals())   
    command = "az security va sql baseline update " + params
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

def set(vm_resource_id, workspace_id, server_name, database_name, baseline=None, latest=None, vm_name=None, agent_id=None, vm_uuid=None):
    params = get_params(locals())   
    command = "az security va sql baseline set " + params
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
