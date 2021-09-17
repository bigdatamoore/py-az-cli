import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def add(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location, type, workspace_id=None):
    params = get_params(locals())   
    command = "az network watcher connection-monitor output add " + params
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

def remove(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location):
    params = get_params(locals())   
    command = "az network watcher connection-monitor output remove " + params
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

def list(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location):
    params = get_params(locals())   
    command = "az network watcher connection-monitor output list " + params
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
