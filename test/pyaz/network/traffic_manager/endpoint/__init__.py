import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, type, name):
    params = get_params(locals())   
    command = "az network traffic-manager endpoint show " + params
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

def delete(resource_group, profile_name, type, name):
    params = get_params(locals())   
    command = "az network traffic-manager endpoint delete " + params
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

def create(resource_group, profile_name, type, name, target_resource_id=None, target=None, endpoint_status=None, weight=None, priority=None, endpoint_location=None, endpoint_monitor_status=None, min_child_endpoints=None, geo_mapping=None, custom_headers=None, subnets=None):
    params = get_params(locals())   
    command = "az network traffic-manager endpoint create " + params
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

def list(resource_group, profile_name, type=None):
    params = get_params(locals())   
    command = "az network traffic-manager endpoint list " + params
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

def update(resource_group, profile_name, type=None, name, endpoint_location=None, endpoint_status=None, endpoint_monitor_status=None, priority=None, target=None, target_resource_id=None, weight=None, min_child_endpoints=None, geo_mapping=None, subnets=None, custom_headers=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network traffic-manager endpoint update " + params
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

def show_geographic_hierarchy():
    params = get_params(locals())   
    command = "az network traffic-manager endpoint show-geographic-hierarchy " + params
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
