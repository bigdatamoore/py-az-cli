import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def add(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location, name, coverage_level=None, type=None, source_test_groups=None, dest_test_groups=None, resource_id=None, address=None, filter_type=None, filter_item=None, address_include=None, address_exclude=None):
    params = get_params(locals())   
    command = "az network watcher connection-monitor endpoint add " + params
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

def remove(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location, name, test_groups=None):
    params = get_params(locals())   
    command = "az network watcher connection-monitor endpoint remove " + params
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

def show(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location, name):
    params = get_params(locals())   
    command = "az network watcher connection-monitor endpoint show " + params
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
    command = "az network watcher connection-monitor endpoint list " + params
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
