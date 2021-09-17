import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def set(feature=None, key=None, name=None, label=None, description=None, yes=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature set " + params
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

def delete(feature=None, key=None, name=None, label=None, yes=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature delete " + params
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

def show(feature=None, key=None, name=None, label=None, fields=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature show " + params
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

def list(feature=None, key=None, name=None, label=None, fields=None, connection_string=None, top=None, all=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature list " + params
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

def lock(feature=None, key=None, name=None, label=None, connection_string=None, yes=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature lock " + params
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

def unlock(feature=None, key=None, name=None, label=None, connection_string=None, yes=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature unlock " + params
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

def enable(feature=None, key=None, name=None, label=None, connection_string=None, yes=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature enable " + params
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

def disable(feature=None, key=None, name=None, label=None, connection_string=None, yes=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig feature disable " + params
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
