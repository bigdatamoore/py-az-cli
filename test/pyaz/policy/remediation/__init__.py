import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(name, management_group=None, resource_group=None, resource=None, namespace=None, parent=None, resource_type=None):
    params = get_params(locals())   
    command = "az policy remediation show " + params
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

def list(management_group=None, resource_group=None, resource=None, namespace=None, parent=None, resource_type=None):
    params = get_params(locals())   
    command = "az policy remediation list " + params
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

def delete(name, management_group=None, resource_group=None, resource=None, namespace=None, parent=None, resource_type=None):
    params = get_params(locals())   
    command = "az policy remediation delete " + params
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

def cancel(name, management_group=None, resource_group=None, resource=None, namespace=None, parent=None, resource_type=None):
    params = get_params(locals())   
    command = "az policy remediation cancel " + params
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

def create(name, policy_assignment, definition_reference_id=None, location_filters=None, management_group=None, resource_group=None, resource=None, namespace=None, parent=None, resource_type=None, resource_discovery_mode=None):
    params = get_params(locals())   
    command = "az policy remediation create " + params
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
