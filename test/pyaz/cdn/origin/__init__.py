import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, endpoint_name, name):
    params = get_params(locals())   
    command = "az cdn origin show " + params
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

def list(resource_group, profile_name, endpoint_name):
    params = get_params(locals())   
    command = "az cdn origin list " + params
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

def create(resource_group, profile_name, endpoint_name, name, host_name, disabled=None, http_port=None, https_port=None, origin_host_header=None, priority=None, weight=None, private_link_resource_id=None, private_link_location=None, private_link_approval_message=None):
    params = get_params(locals())   
    command = "az cdn origin create " + params
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

def update(resource_group, profile_name, endpoint_name, name, host_name=None, http_port=None, https_port=None, disabled=None, origin_host_header=None, priority=None, weight=None, private_link_resource_id=None, private_link_location=None, private_link_approval_message=None):
    params = get_params(locals())   
    command = "az cdn origin update " + params
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

def delete(resource_group, profile_name, endpoint_name, name, yes=None):
    params = get_params(locals())   
    command = "az cdn origin delete " + params
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
