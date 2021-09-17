import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, endpoint_name):
    params = get_params(locals())   
    command = "az cdn endpoint waf policy show " + params
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

def set(resource_group, profile_name, endpoint_name, waf_policy_subscription_id=None, waf_policy_resource_group_name=None, waf_policy_name=None, waf_policy_id=None):
    params = get_params(locals())   
    command = "az cdn endpoint waf policy set " + params
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

def remove(resource_group, profile_name, endpoint_name, yes=None):
    params = get_params(locals())   
    command = "az cdn endpoint waf policy remove " + params
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
