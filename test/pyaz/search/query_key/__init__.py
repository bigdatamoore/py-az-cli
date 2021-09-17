import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group, service_name, __SEARCH_MANAGEMENT_REQUEST_OPTIONS=None):
    params = get_params(locals())   
    command = "az search query-key list " + params
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

def create(resource_group, service_name, name, __SEARCH_MANAGEMENT_REQUEST_OPTIONS=None):
    params = get_params(locals())   
    command = "az search query-key create " + params
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

def delete(resource_group, service_name, key_value, __SEARCH_MANAGEMENT_REQUEST_OPTIONS=None):
    params = get_params(locals())   
    command = "az search query-key delete " + params
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
