import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(lb_name=None, gateway_name=None, resource_group, nic_name, name, subnet=None, vnet_name=None, public_ip_address=None, lb_address_pools=None, lb_inbound_nat_rules=None, private_ip_address=None, private_ip_address_version=None, make_primary=None, application_security_groups=None, app_gateway_address_pools=None):
    params = get_params(locals())   
    command = "az network nic ip-config create " + params
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

def update(lb_name=None, gateway_name=None, resource_group, nic_name, gateway_lb=None, name, subnet=None, vnet_name=None, public_ip_address=None, lb_address_pools=None, lb_inbound_nat_rules=None, private_ip_address=None, private_ip_address_version=None, make_primary=None, application_security_groups=None, app_gateway_address_pools=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network nic ip-config update " + params
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

def list(resource_group, nic_name):
    params = get_params(locals())   
    command = "az network nic ip-config list " + params
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

def show(resource_group, nic_name, name):
    params = get_params(locals())   
    command = "az network nic ip-config show " + params
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

def delete(resource_group, nic_name, name):
    params = get_params(locals())   
    command = "az network nic ip-config delete " + params
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
