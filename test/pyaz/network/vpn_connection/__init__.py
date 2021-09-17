import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, name, vnet_gateway1, location=None, tags=None, validate=None, vnet_gateway2=None, express_route_circuit2=None, local_gateway2=None, authorization_key=None, enable_bgp=None, routing_weight=None, __CONNECTION_TYPE=None, shared_key=None, use_policy_based_traffic_selectors=None, express_route_gateway_bypass=None, ingress_nat_rule=None, egress_nat_rule=None):
    params = get_params(locals())   
    command = "az network vpn-connection create " + params
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

def delete(resource_group, name):
    params = get_params(locals())   
    command = "az network vpn-connection delete " + params
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

def show(resource_group, name):
    params = get_params(locals())   
    command = "az network vpn-connection show " + params
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

def list(resource_group, vnet_gateway=None):
    params = get_params(locals())   
    command = "az network vpn-connection list " + params
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

def update(resource_group, name, routing_weight=None, shared_key=None, tags=None, enable_bgp=None, use_policy_based_traffic_selectors=None, express_route_gateway_bypass=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network vpn-connection update " + params
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

def list_ike_sas(resource_group, name):
    params = get_params(locals())   
    command = "az network vpn-connection list-ike-sas " + params
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

def show_device_config_script(resource_group, name, vendor, device_family, firmware_version):
    params = get_params(locals())   
    command = "az network vpn-connection show-device-config-script " + params
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
