import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(account_name, resource_group, name, identifier=None, base64_key=None, expiration=None):
    params = get_params(locals())   
    command = "az ams streaming-endpoint akamai add " + params
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

def remove(account_name, resource_group, name, identifier):
    params = get_params(locals())   
    command = "az ams streaming-endpoint akamai remove " + params
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
