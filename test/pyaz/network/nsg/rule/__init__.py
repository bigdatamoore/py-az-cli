import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def delete(resource_group, nsg_name, name):
    params = get_params(locals())   
    command = "az network nsg rule delete " + params
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

def list(resource_group, nsg_name, include_default=None):
    params = get_params(locals())   
    command = "az network nsg rule list " + params
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

def show(resource_group, nsg_name, name):
    params = get_params(locals())   
    command = "az network nsg rule show " + params
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

def create(resource_group, nsg_name, name, priority, description=None, protocol=None, access=None, direction=None, source_port_ranges=None, source_address_prefixes=None, destination_port_ranges=None, destination_address_prefixes=None, source_asgs=None, destination_asgs=None):
    params = get_params(locals())   
    command = "az network nsg rule create " + params
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

def update(resource_group, nsg_name, name, protocol=None, source_address_prefixes=None, destination_address_prefixes=None, access=None, direction=None, description=None, source_port_ranges=None, destination_port_ranges=None, priority=None, source_asgs=None, destination_asgs=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network nsg rule update " + params
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
