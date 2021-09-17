import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(filter_name, feature=None, key=None, name=None, label=None, filter_parameters=None, yes=None, index=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature filter add " + params
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

def delete(feature=None, key=None, filter_name=None, name=None, label=None, index=None, yes=None, connection_string=None, all=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature filter delete " + params
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

def show(filter_name, feature=None, key=None, index=None, name=None, label=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature filter show " + params
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

def list(feature=None, key=None, name=None, label=None, connection_string=None, top=None, all=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature filter list " + params
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
