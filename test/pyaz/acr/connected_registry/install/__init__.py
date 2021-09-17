import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def info(name, registry, parent_protocol, resource_group=None):
    params = get_params(locals())   
    command = "az acr connected-registry install info " + params
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

def renew_credentials(name, registry, parent_protocol, resource_group=None):
    params = get_params(locals())   
    command = "az acr connected-registry install renew-credentials " + params
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
