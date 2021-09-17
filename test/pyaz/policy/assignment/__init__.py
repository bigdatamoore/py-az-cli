import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(policy=None, policy_set_definition=None, name=None, display_name=None, params=None, resource_group=None, scope=None, sku=None, not_scopes=None, location=None, assign_identity=None, identity_scope=None, role=None, enforcement_mode=None, description=None):
    params = get_params(locals())   
    command = "az policy assignment create " + params
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

def delete(name, resource_group=None, scope=None):
    params = get_params(locals())   
    command = "az policy assignment delete " + params
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

def list(disable_scope_strict_match=None, resource_group=None, scope=None):
    params = get_params(locals())   
    command = "az policy assignment list " + params
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

def show(name, resource_group=None, scope=None):
    params = get_params(locals())   
    command = "az policy assignment show " + params
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

def update(name=None, display_name=None, params=None, resource_group=None, scope=None, sku=None, not_scopes=None, enforcement_mode=None, description=None):
    params = get_params(locals())   
    command = "az policy assignment update " + params
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
