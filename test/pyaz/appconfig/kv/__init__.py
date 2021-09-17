import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def set(key, name=None, label=None, content_type=None, tags=None, value=None, yes=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig kv set " + params
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

def delete(key, name=None, label=None, yes=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig kv delete " + params
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

def show(key, name=None, label=None, datetime=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig kv show " + params
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

def list(key=None, fields=None, name=None, label=None, datetime=None, connection_string=None, top=None, all=None, resolve_keyvault=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig kv list " + params
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

def lock(key, label=None, name=None, connection_string=None, yes=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig kv lock " + params
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

def unlock(key, label=None, name=None, connection_string=None, yes=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig kv unlock " + params
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

def restore(datetime, key=None, name=None, label=None, connection_string=None, yes=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig kv restore " + params
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

def import_(source, name=None, connection_string=None, label=None, prefix=None, yes=None, skip_features=None, content_type=None, auth_mode=None, endpoint=None, path=None, format=None, separator=None, depth=None, src_name=None, src_connection_string=None, src_key=None, src_label=None, preserve_labels=None, src_auth_mode=None, src_endpoint=None, appservice_account=None):
    params = get_params(locals())   
    command = "az appconfig kv import " + params
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

def export(destination, name=None, connection_string=None, label=None, key=None, prefix=None, yes=None, skip_features=None, skip_keyvault=None, auth_mode=None, endpoint=None, path=None, format=None, separator=None, naming_convention=None, resolve_keyvault=None, dest_name=None, dest_connection_string=None, dest_label=None, preserve_labels=None, dest_auth_mode=None, dest_endpoint=None, appservice_account=None):
    params = get_params(locals())   
    command = "az appconfig kv export " + params
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

def set_keyvault(key, secret_identifier, name=None, label=None, tags=None, yes=None, connection_string=None, auth_mode=None, endpoint=None):
    params = get_params(locals())   
    command = "az appconfig kv set-keyvault " + params
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
