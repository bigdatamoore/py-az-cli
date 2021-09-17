import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, name, expand=None):
    params = get_params(locals())   
    command = "az network cross-region-lb show " + params
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

def create(name, resource_group, location=None, tags=None, backend_pool_name=None, frontend_ip_name=None, public_ip_address=None, public_ip_address_allocation=None, public_ip_dns_name=None, __PUBLIC_IP_ADDRESS_TYPE=None, validate=None, frontend_ip_zone=None, public_ip_zone=None, no_wait=None):
    params = get_params(locals())   
    command = "az network cross-region-lb create " + params
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
    command = "az network cross-region-lb delete " + params
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

def list(resource_group=None):
    params = get_params(locals())   
    command = "az network cross-region-lb list " + params
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

def update(resource_group, name, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network cross-region-lb update " + params
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

def wait(resource_group, name, expand=None, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az network cross-region-lb wait " + params
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
