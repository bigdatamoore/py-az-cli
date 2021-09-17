import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def set(resource_group, name, sa_lifetime, sa_max_size, ipsec_encryption, ipsec_integrity, ike_encryption, ike_integrity, dh_group, pfs_group, no_wait=None):
    params = get_params(locals())   
    command = "az network vnet-gateway vpn-client ipsec-policy set " + params
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
    command = "az network vnet-gateway vpn-client ipsec-policy show " + params
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
