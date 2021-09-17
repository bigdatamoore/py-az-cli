import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(resource_group, vnet_name, name, address_prefixes, network_security_group=None, route_table=None, service_endpoints=None, service_endpoint_policy=None, delegations=None, nat_gateway=None, disable_private_endpoint_network_policies=None, disable_private_link_service_network_policies=None):
    params = get_params(locals())   
    command = "az network vnet subnet create " + params
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

def delete(resource_group, vnet_name, name):
    params = get_params(locals())   
    command = "az network vnet subnet delete " + params
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

def show(resource_group, vnet_name, name, expand=None):
    params = get_params(locals())   
    command = "az network vnet subnet show " + params
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

def list(resource_group, vnet_name):
    params = get_params(locals())   
    command = "az network vnet subnet list " + params
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

def update(resource_group, vnet_name, name, address_prefixes=None, network_security_group=None, route_table=None, service_endpoints=None, delegations=None, nat_gateway=None, service_endpoint_policy=None, disable_private_endpoint_network_policies=None, disable_private_link_service_network_policies=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network vnet subnet update " + params
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

def list_available_delegations(resource_group=None, location=None):
    params = get_params(locals())   
    command = "az network vnet subnet list-available-delegations " + params
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
