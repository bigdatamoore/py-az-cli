import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, name, resource, logs=None, metrics=None, event_hub=None, event_hub_rule=None, storage_account=None, workspace=None, export_to_resource_specific=None):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings create " + params
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

def show(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, resource, name):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings show " + params
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

def list(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, resource):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings list " + params
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

def delete(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, resource, name):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings delete " + params
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

def update(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, resource, name, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings update " + params
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
