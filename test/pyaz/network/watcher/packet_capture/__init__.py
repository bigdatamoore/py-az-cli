import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(resource_group, name, vm, __WATCHER_RG=None, __WATCHER_NAME=None, __LOCATION=None, storage_account=None, storage_path=None, file_path=None, capture_size=None, capture_limit=None, time_limit=None, filters=None):
    params = get_params(locals())   
    command = "az network watcher packet-capture create " + params
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

def show(location, __RESOURCE_GROUP_NAME=None, network_watcher_name=None, name):
    params = get_params(locals())   
    command = "az network watcher packet-capture show " + params
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

def show_status(location, __RESOURCE_GROUP_NAME=None, network_watcher_name=None, name):
    params = get_params(locals())   
    command = "az network watcher packet-capture show-status " + params
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

def delete(location, __RESOURCE_GROUP_NAME=None, network_watcher_name=None, name):
    params = get_params(locals())   
    command = "az network watcher packet-capture delete " + params
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

def stop(location, __RESOURCE_GROUP_NAME=None, network_watcher_name=None, name):
    params = get_params(locals())   
    command = "az network watcher packet-capture stop " + params
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

def list(location, __RESOURCE_GROUP_NAME=None, network_watcher_name=None):
    params = get_params(locals())   
    command = "az network watcher packet-capture list " + params
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
