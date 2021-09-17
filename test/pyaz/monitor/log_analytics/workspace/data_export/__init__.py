import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def list(resource_group, workspace_name):
    params = get_params(locals())   
    command = "az monitor log-analytics workspace data-export list " + params
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

def show(resource_group, workspace_name, name):
    params = get_params(locals())   
    command = "az monitor log-analytics workspace data-export show " + params
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

def create(workspace_name, resource_group, name, destination, __DATA_EXPORT_TYPE=None, tables, __EVENT_HUB_NAME=None, enable=None):
    params = get_params(locals())   
    command = "az monitor log-analytics workspace data-export create " + params
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

def update(resource_group, workspace_name, name, tables, destination=None, __DATA_EXPORT_TYPE=None, __EVENT_HUB_NAME=None, enable=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az monitor log-analytics workspace data-export update " + params
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

def delete(resource_group, workspace_name, name, yes=None):
    params = get_params(locals())   
    command = "az monitor log-analytics workspace data-export delete " + params
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
