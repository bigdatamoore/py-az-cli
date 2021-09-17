import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(registry, name, repository=None, sync_token=None, client_tokens=None, resource_group=None, mode=None, parent=None, sync_schedule=None, sync_message_ttl=None, sync_window=None, log_level=None, audit_logs_enabled=None):
    params = get_params(locals())   
    command = "az acr connected-registry create " + params
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

def delete(name, registry, cleanup=None, yes=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr connected-registry delete " + params
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

def show(name, registry, resource_group=None):
    params = get_params(locals())   
    command = "az acr connected-registry show " + params
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

def deactivate(name, registry, yes=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr connected-registry deactivate " + params
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

def update(registry, name, add_client_tokens=None, remove_client_tokens=None, resource_group=None, sync_schedule=None, sync_window=None, log_level=None, sync_message_ttl=None, audit_logs_enabled=None):
    params = get_params(locals())   
    command = "az acr connected-registry update " + params
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

def repo(name, registry, add=None, remove=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr connected-registry repo " + params
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

def list(registry, parent=None, no_children=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr connected-registry list " + params
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

def list_client_tokens(name, registry, resource_group=None):
    params = get_params(locals())   
    command = "az acr connected-registry list-client-tokens " + params
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
