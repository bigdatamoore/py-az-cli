import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def create(resource_group, gateway_name, rule_set_name, rule_name, variable, pattern=None, ignore_case=None, negate=None, no_wait=None):
    params = get_params(locals())   
    command = "az network application-gateway rewrite-rule condition create " + params
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

def show(resource_group, gateway_name, rule_set_name, rule_name, variable):
    params = get_params(locals())   
    command = "az network application-gateway rewrite-rule condition show " + params
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

def list(resource_group, gateway_name, rule_set_name, rule_name):
    params = get_params(locals())   
    command = "az network application-gateway rewrite-rule condition list " + params
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

def delete(resource_group, gateway_name, rule_set_name, rule_name, variable, no_wait=None):
    params = get_params(locals())   
    command = "az network application-gateway rewrite-rule condition delete " + params
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

def update(resource_group, gateway_name, rule_set_name, rule_name, variable, pattern=None, ignore_case=None, negate=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az network application-gateway rewrite-rule condition update " + params
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

def list_server_variables():
    params = get_params(locals())   
    command = "az network application-gateway rewrite-rule condition list-server-variables " + params
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
