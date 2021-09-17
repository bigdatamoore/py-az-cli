import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, lb_name):
    params = get_params(locals())   
    command = "az network lb inbound-nat-rule list " + params
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
    command = "az network lb inbound-nat-rule show " + params
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
    command = "az network lb inbound-nat-rule delete " + params
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

def create(resource_group, lb_name, name, protocol, frontend_port, backend_port, frontend_ip_name=None, floating_ip=None, idle_timeout=None, enable_tcp_reset=None):
    params = get_params(locals())   
    command = "az network lb inbound-nat-rule create " + params
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

def update(resource_group, lb_name, name, protocol=None, frontend_port=None, frontend_ip_name=None, backend_port=None, floating_ip=None, idle_timeout=None, enable_tcp_reset=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network lb inbound-nat-rule update " + params
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
