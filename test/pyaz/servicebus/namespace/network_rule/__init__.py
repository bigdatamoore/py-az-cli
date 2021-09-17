import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(vnet_name=None, resource_group, namespace_name, subnet=None, ip_address=None, ignore_missing_endpoint=None, action=None):
    params = get_params(locals())   
    command = "az servicebus namespace network-rule add " + params
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

def list(resource_group, namespace_name):
    params = get_params(locals())   
    command = "az servicebus namespace network-rule list " + params
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

def remove(vnet_name=None, resource_group, namespace_name, subnet=None, ip_address=None):
    params = get_params(locals())   
    command = "az servicebus namespace network-rule remove " + params
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
