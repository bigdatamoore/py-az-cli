import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def delete(registry, name, password1=None, password2=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr token credential delete " + params
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

def generate(registry, name, password1=None, password2=None, expiration_in_days=None, expiration=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr token credential generate " + params
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
