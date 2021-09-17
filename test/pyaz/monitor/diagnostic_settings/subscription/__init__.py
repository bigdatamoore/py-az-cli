import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(name, logs, location, event_hub_name=None, event_hub_auth_rule=None, storage_account=None, service_bus_rule=None, workspace=None):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings subscription create " + params
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

def delete(subscription_id=None, name, yes=None):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings subscription delete " + params
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

def show(subscription_id=None, name):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings subscription show " + params
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

def list(subscription_id=None):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings subscription list " + params
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

def update(subscription_id=None, name, event_hub_name=None, logs=None, event_hub_auth_rule=None, storage_account=None, service_bus_rule=None, workspace=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az monitor diagnostic-settings subscription update " + params
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
