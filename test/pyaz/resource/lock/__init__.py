import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(name, lock_type, resource_group=None, namespace=None, notes=None, parent=None, resource_type=None, resource=None):
    params = get_params(locals())   
    command = "az resource lock create " + params
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

def delete(name=None, resource_group=None, namespace=None, parent=None, resource_type=None, resource=None, ids=None):
    params = get_params(locals())   
    command = "az resource lock delete " + params
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

def list(resource_group=None, namespace=None, parent=None, resource_type=None, resource=None, filter_string=None):
    params = get_params(locals())   
    command = "az resource lock list " + params
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

def show(name=None, resource_group=None, namespace=None, parent=None, resource_type=None, resource=None, ids=None):
    params = get_params(locals())   
    command = "az resource lock show " + params
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

def update(name=None, resource_group=None, namespace=None, notes=None, parent=None, resource_type=None, resource=None, lock_type=None, ids=None):
    params = get_params(locals())   
    command = "az resource lock update " + params
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
