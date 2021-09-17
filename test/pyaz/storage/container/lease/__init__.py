import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def acquire(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, lease_duration=None, proposed_lease_id=None, if_modified_since=None, if_unmodified_since=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container lease acquire " + params
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

def renew(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, lease_id, if_modified_since=None, if_unmodified_since=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container lease renew " + params
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

def release(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, lease_id, if_modified_since=None, if_unmodified_since=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container lease release " + params
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

def change(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, lease_id, proposed_lease_id, if_modified_since=None, if_unmodified_since=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container lease change " + params
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

def break_(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, lease_break_period=None, if_modified_since=None, if_unmodified_since=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container lease break " + params
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
