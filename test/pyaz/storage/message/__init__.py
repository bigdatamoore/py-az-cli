import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def put(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, queue_name, content, visibility_timeout=None, time_to_live=None, timeout=None):
    params = get_params(locals())   
    command = "az storage message put " + params
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

def get(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, queue_name, num_messages=None, visibility_timeout=None, timeout=None):
    params = get_params(locals())   
    command = "az storage message get " + params
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

def peek(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, queue_name, num_messages=None, timeout=None):
    params = get_params(locals())   
    command = "az storage message peek " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, queue_name, id, pop_receipt, timeout=None):
    params = get_params(locals())   
    command = "az storage message delete " + params
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

def clear(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, queue_name, timeout=None):
    params = get_params(locals())   
    command = "az storage message clear " + params
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

def update(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, queue_name, id, pop_receipt, visibility_timeout, content=None, timeout=None):
    params = get_params(locals())   
    command = "az storage message update " + params
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
