import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def set(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, owner=None, group=None, permissions=None, acl=None):
    params = get_params(locals())   
    command = "az storage fs access set " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, __UPN=None):
    params = get_params(locals())   
    command = "az storage fs access show " + params
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

def set_recursive(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None, continuation=None, batch_size=None, max_batches=None, continue_on_failure=None, acl):
    params = get_params(locals())   
    command = "az storage fs access set-recursive " + params
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

def update_recursive(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None, continuation=None, batch_size=None, max_batches=None, continue_on_failure=None, acl):
    params = get_params(locals())   
    command = "az storage fs access update-recursive " + params
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

def remove_recursive(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None, continuation=None, batch_size=None, max_batches=None, continue_on_failure=None, acl):
    params = get_params(locals())   
    command = "az storage fs access remove-recursive " + params
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
