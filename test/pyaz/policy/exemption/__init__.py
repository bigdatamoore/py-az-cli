import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(name, policy_assignment=None, exemption_category=None, policy_definition_reference_ids=None, expires_on=None, display_name=None, description=None, resource_group=None, scope=None, metadata=None):
    params = get_params(locals())   
    command = "az policy exemption create " + params
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
    command = "az policy exemption delete " + params
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
    command = "az policy exemption list " + params
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
    command = "az policy exemption show " + params
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

def update(name, exemption_category=None, policy_definition_reference_ids=None, expires_on=None, display_name=None, description=None, resource_group=None, scope=None, metadata=None):
    params = get_params(locals())   
    command = "az policy exemption update " + params
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
