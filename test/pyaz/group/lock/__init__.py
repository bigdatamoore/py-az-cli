import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(name, lock_type, resource_group, __RESOURCE_PROVIDER_NAMESPACE=None, notes=None, __PARENT_RESOURCE_PATH=None, __RESOURCE_TYPE=None, __RESOURCE_NAME=None):
    params = get_params(locals())   
    command = "az group lock create " + params
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

def delete(name=None, resource_group=None, __RESOURCE_PROVIDER_NAMESPACE=None, __PARENT_RESOURCE_PATH=None, __RESOURCE_TYPE=None, __RESOURCE_NAME=None, ids=None):
    params = get_params(locals())   
    command = "az group lock delete " + params
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

def list(resource_group=None, __RESOURCE_PROVIDER_NAMESPACE=None, __PARENT_RESOURCE_PATH=None, __RESOURCE_TYPE=None, __RESOURCE_NAME=None, filter_string=None):
    params = get_params(locals())   
    command = "az group lock list " + params
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

def show(name=None, resource_group=None, __RESOURCE_PROVIDER_NAMESPACE=None, __PARENT_RESOURCE_PATH=None, __RESOURCE_TYPE=None, __RESOURCE_NAME=None, ids=None):
    params = get_params(locals())   
    command = "az group lock show " + params
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

def update(name=None, resource_group=None, __RESOURCE_PROVIDER_NAMESPACE=None, notes=None, __PARENT_RESOURCE_PATH=None, __RESOURCE_TYPE=None, __RESOURCE_NAME=None, lock_type=None, ids=None):
    params = get_params(locals())   
    command = "az group lock update " + params
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
