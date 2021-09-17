import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, gateway_name, sa_lifetime, sa_max_size, ipsec_encryption, ipsec_integrity, ike_encryption, ike_integrity, dh_group, pfs_group, no_wait=None):
    params = get_params(locals())   
    command = "az network vnet-gateway ipsec-policy add " + params
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

def list(resource_group, gateway_name):
    params = get_params(locals())   
    command = "az network vnet-gateway ipsec-policy list " + params
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

def clear(resource_group, gateway_name, no_wait=None):
    params = get_params(locals())   
    command = "az network vnet-gateway ipsec-policy clear " + params
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
