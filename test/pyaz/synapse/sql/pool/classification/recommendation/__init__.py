import json, subprocess
from ...... pyaz_utils import get_cli_name, get_params


def list(resource_group, workspace_name, name, included_disabled=None, skip_token=None, filter=None):
    params = get_params(locals())   
    command = "az synapse sql pool classification recommendation list " + params
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

def enable(resource_group, workspace_name, name, schema, table, column):
    params = get_params(locals())   
    command = "az synapse sql pool classification recommendation enable " + params
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

def disable(resource_group, workspace_name, name, schema, table, column):
    params = get_params(locals())   
    command = "az synapse sql pool classification recommendation disable " + params
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
