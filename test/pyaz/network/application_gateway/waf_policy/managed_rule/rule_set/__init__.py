import json, subprocess
from ...... pyaz_utils import get_cli_name, get_params


def add(resource_group, policy_name, type, version, group_name=None, rules=None):
    params = get_params(locals())   
    command = "az network application-gateway waf-policy managed-rule rule-set add " + params
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

def update(resource_group, policy_name, type, version, group_name=None, rules=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network application-gateway waf-policy managed-rule rule-set update " + params
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

def remove(resource_group, policy_name, type, version, group_name=None):
    params = get_params(locals())   
    command = "az network application-gateway waf-policy managed-rule rule-set remove " + params
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

def list(resource_group, policy_name):
    params = get_params(locals())   
    command = "az network application-gateway waf-policy managed-rule rule-set list " + params
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
