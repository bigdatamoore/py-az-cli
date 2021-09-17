import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, name, timeout=None, permissions=None, umask=None, metadata=None):
    params = get_params(locals())   
    command = "az storage fs directory create " + params
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

def exists(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, name, timeout=None):
    params = get_params(locals())   
    command = "az storage fs directory exists " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, name, timeout=None):
    params = get_params(locals())   
    command = "az storage fs directory show " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, name, timeout=None, yes=None):
    params = get_params(locals())   
    command = "az storage fs directory delete " + params
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

def move(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, name, timeout=None, new_directory):
    params = get_params(locals())   
    command = "az storage fs directory move " + params
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

def list(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, path=None, recursive=None, num_results=None, timeout=None):
    params = get_params(locals())   
    command = "az storage fs directory list " + params
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

def upload(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, file_system, destination_path=None, source, __DESTINATION=None, recursive=None):
    params = get_params(locals())   
    command = "az storage fs directory upload " + params
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

def download(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, file_system, source_path=None, __SOURCE=None, destination_path, recursive=None):
    params = get_params(locals())   
    command = "az storage fs directory download " + params
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
