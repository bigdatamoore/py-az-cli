import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def start(__WATCHER_NAME=None, __WATCHER_RG=None, resource, storage_account, storage_path, resource_type=None, resource_group=None, no_wait=None):
    params = get_params(locals())   
    command = "az network watcher troubleshooting start " + params
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

def show(__WATCHER_NAME=None, __WATCHER_RG=None, resource, resource_type=None, resource_group=None):
    params = get_params(locals())   
    command = "az network watcher troubleshooting show " + params
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
