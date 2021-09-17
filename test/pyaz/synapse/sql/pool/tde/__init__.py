import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def set(name, workspace_name, resource_group, transparent_data_encryption_name, status):
    params = get_params(locals())   
    command = "az synapse sql pool tde set " + params
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

def show(resource_group, workspace_name, name, transparent_data_encryption_name):
    params = get_params(locals())   
    command = "az synapse sql pool tde show " + params
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
