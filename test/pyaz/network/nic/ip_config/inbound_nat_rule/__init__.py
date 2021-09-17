import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def add(resource_group, nic_name, ip_config_name, inbound_nat_rule, lb_name=None):
    params = get_params(locals())   
    command = "az network nic ip-config inbound-nat-rule add " + params
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

def remove(resource_group, nic_name, ip_config_name, inbound_nat_rule, lb_name=None):
    params = get_params(locals())   
    command = "az network nic ip-config inbound-nat-rule remove " + params
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
