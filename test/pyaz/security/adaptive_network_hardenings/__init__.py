import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(adaptive_network_hardenings_resource_name, resource_name, resource_type, resource_namespace, resource_group):
    params = get_params(locals())   
    command = "az security adaptive_network_hardenings show " + params
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

def list(resource_name, resource_type, resource_namespace, resource_group):
    params = get_params(locals())   
    command = "az security adaptive_network_hardenings list " + params
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
