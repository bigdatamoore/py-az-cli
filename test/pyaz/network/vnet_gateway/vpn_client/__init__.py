import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def generate(resource_group, name, processor_architecture=None, authentication_method=None, radius_server_auth_certificate=None, client_root_certificates=None, use_legacy=None):
    params = get_params(locals())   
    command = "az network vnet-gateway vpn-client generate " + params
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

def show_url(resource_group, name):
    params = get_params(locals())   
    command = "az network vnet-gateway vpn-client show-url " + params
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

def show_health(resource_group, name):
    params = get_params(locals())   
    command = "az network vnet-gateway vpn-client show-health " + params
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
