import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, resource, name):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings categories show " + params
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

def list(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, resource):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings categories list " + params
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
