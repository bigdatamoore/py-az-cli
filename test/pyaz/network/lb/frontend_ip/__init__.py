import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, lb_name):
    params = get_params(locals())   
    command = "az network lb frontend-ip list " + params
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

def show(resource_group, lb_name, name):
    params = get_params(locals())   
    command = "az network lb frontend-ip show " + params
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

def delete(resource_group, lb_name, name):
    params = get_params(locals())   
    command = "az network lb frontend-ip delete " + params
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

def create(resource_group, lb_name, name, public_ip_address=None, public_ip_prefix=None, subnet=None, vnet_name=None, private_ip_address=None, private_ip_address_version=None, __PRIVATE_IP_ADDRESS_ALLOCATION=None, zone=None):
    params = get_params(locals())   
    command = "az network lb frontend-ip create " + params
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

def update(resource_group, lb_name, gateway_lb=None, name, private_ip_address=None, __PRIVATE_IP_ADDRESS_ALLOCATION=None, public_ip_address=None, subnet=None, vnet_name=None, public_ip_prefix=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network lb frontend-ip update " + params
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
