import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def configure(__WATCHER_RG=None, __WATCHER_NAME=None, nsg, storage_account=None, resource_group=None, enabled=None, retention=None, format=None, log_version=None, workspace=None, interval=None, traffic_analytics=None):
    params = get_params(locals())   
    command = "az network watcher flow-log configure " + params
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

def show(__WATCHER_RG=None, __WATCHER_NAME=None, location=None, resource_group=None, nsg=None, name=None):
    params = get_params(locals())   
    command = "az network watcher flow-log show " + params
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

def list(__WATCHER_RG=None, __WATCHER_NAME=None, location):
    params = get_params(locals())   
    command = "az network watcher flow-log list " + params
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

def delete(__WATCHER_RG=None, __WATCHER_NAME=None, location, name):
    params = get_params(locals())   
    command = "az network watcher flow-log delete " + params
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

def create(location, __WATCHER_RG=None, __WATCHER_NAME=None, name, nsg, storage_account=None, resource_group=None, enabled=None, retention=None, format=None, log_version=None, workspace=None, interval=None, traffic_analytics=None, tags=None):
    params = get_params(locals())   
    command = "az network watcher flow-log create " + params
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

def update(__WATCHER_RG=None, __WATCHER_NAME=None, name, location, resource_group=None, enabled=None, nsg=None, storage_account=None, retention=None, format=None, log_version=None, workspace=None, interval=None, traffic_analytics=None, tags=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network watcher flow-log update " + params
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
