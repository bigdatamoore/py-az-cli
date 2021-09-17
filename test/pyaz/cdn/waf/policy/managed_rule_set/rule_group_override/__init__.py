import json, subprocess
from ...... pyaz_utils import get_cli_name, get_params


def set(resource_group, policy_name, rule_set_type, rule_set_version, name, _r):
    params = get_params(locals())   
    command = "az cdn waf policy managed-rule-set rule-group-override set " + params
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

def delete(resource_group, policy_name, rule_set_type, rule_set_version, name, yes=None):
    params = get_params(locals())   
    command = "az cdn waf policy managed-rule-set rule-group-override delete " + params
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

def list(resource_group, policy_name, rule_set_type, rule_set_version):
    params = get_params(locals())   
    command = "az cdn waf policy managed-rule-set rule-group-override list " + params
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

def show(resource_group, policy_name, rule_set_type, rule_set_version, name):
    params = get_params(locals())   
    command = "az cdn waf policy managed-rule-set rule-group-override show " + params
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

def list_available(rule_set_type, rule_set_version):
    params = get_params(locals())   
    command = "az cdn waf policy managed-rule-set rule-group-override list-available " + params
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
