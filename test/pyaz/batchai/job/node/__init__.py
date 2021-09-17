import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, workspace, experiment, job):
    params = get_params(locals())   
    command = "az batchai job node list " + params
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

def exec(resource_group, workspace, experiment, job, node_id=None, address=None, exec=None, password=None, ssh_private_key=None):
    params = get_params(locals())   
    command = "az batchai job node exec " + params
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
