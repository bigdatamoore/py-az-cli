import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(id=None, resource_group=None, scope_name=None, name=None):
    params = get_params(locals())   
    command = "az monitor private-link-scope private-endpoint-connection show " + params
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

def list(resource_group, scope_name):
    params = get_params(locals())   
    command = "az monitor private-link-scope private-endpoint-connection list " + params
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

def approve(id=None, resource_group=None, scope_name=None, name=None, description=None):
    params = get_params(locals())   
    command = "az monitor private-link-scope private-endpoint-connection approve " + params
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

def reject(id=None, resource_group=None, scope_name=None, name=None, description=None):
    params = get_params(locals())   
    command = "az monitor private-link-scope private-endpoint-connection reject " + params
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

def delete(id=None, resource_group=None, scope_name=None, name=None, yes=None):
    params = get_params(locals())   
    command = "az monitor private-link-scope private-endpoint-connection delete " + params
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
