import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, origin_group_name, origin_name):
    params = get_params(locals())   
    command = "az afd origin show " + params
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

def list(resource_group, profile_name, origin_group_name):
    params = get_params(locals())   
    command = "az afd origin list " + params
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

def create(resource_group, profile_name, origin_group_name, origin_name, host_name, enabled_state, enable_private_link=None, private_link_resource=None, private_link_location=None, private_link_sub_resource_type=None, private_link_request_message=None, http_port=None, https_port=None, origin_host_header=None, priority=None, weight=None):
    params = get_params(locals())   
    command = "az afd origin create " + params
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

def update(resource_group, profile_name, origin_group_name, origin_name, host_name=None, enabled_state=None, http_port=None, https_port=None, origin_host_header=None, priority=None, weight=None, enable_private_link=None, private_link_resource=None, private_link_location=None, private_link_sub_resource_type=None, private_link_request_message=None):
    params = get_params(locals())   
    command = "az afd origin update " + params
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

def delete(resource_group, profile_name, origin_group_name, origin_name, yes=None):
    params = get_params(locals())   
    command = "az afd origin delete " + params
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
