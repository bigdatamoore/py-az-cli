import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(resource_group, zone_name, name, record_type=None):
    params = get_params(locals())   
    command = "az network dns record-set ns show " + params
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

def delete(resource_group, zone_name, name, record_type=None, if_match=None, yes=None):
    params = get_params(locals())   
    command = "az network dns record-set ns delete " + params
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

def list(resource_group, zone_name, record_type=None):
    params = get_params(locals())   
    command = "az network dns record-set ns list " + params
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

def create(resource_group, zone_name, name, record_set_type=None, metadata=None, if_match=None, if_none_match=None, ttl=None, target_resource=None):
    params = get_params(locals())   
    command = "az network dns record-set ns create " + params
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

def add_record(resource_group, zone_name, record_set_name, nsdname, subscriptionid=None, ttl=None, if_none_match=None):
    params = get_params(locals())   
    command = "az network dns record-set ns add-record " + params
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

def remove_record(resource_group, zone_name, record_set_name, nsdname, keep_empty_record_set=None):
    params = get_params(locals())   
    command = "az network dns record-set ns remove-record " + params
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

def update(resource_group, zone_name, name, record_type=None, if_match=None, if_none_match=None, metadata=None, target_resource=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network dns record-set ns update " + params
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
