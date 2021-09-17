import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_group, name, slot=None):
    params = get_params(locals())   
    command = "az functionapp config access-restriction show " + params
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

def add(resource_group, name, priority, rule_name=None, action=None, ip_address=None, subnet=None, vnet_name=None, description=None, scm_site=None, ignore_missing_endpoint=None, slot=None, vnet_resource_group=None, service_tag=None, http_headers=None):
    params = get_params(locals())   
    command = "az functionapp config access-restriction add " + params
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

def remove(resource_group, name, rule_name=None, action=None, ip_address=None, subnet=None, vnet_name=None, scm_site=None, slot=None, service_tag=None):
    params = get_params(locals())   
    command = "az functionapp config access-restriction remove " + params
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

def set(resource_group, name, use_same_restrictions_for_scm_site, slot=None):
    params = get_params(locals())   
    command = "az functionapp config access-restriction set " + params
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
