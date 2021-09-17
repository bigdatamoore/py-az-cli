import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, metadata=None, fail_on_exist=None, timeout=None):
    params = get_params(locals())   
    command = "az storage queue create " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, fail_not_exist=None, timeout=None):
    params = get_params(locals())   
    command = "az storage queue delete " + params
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

def generate_sas(account_name=None, account_key=None, connection_string=None, __SAS_TOKEN=None, __AUTH_MODE=None, name, permissions=None, expiry=None, start=None, policy_name=None, ip=None, https_only=None):
    params = get_params(locals())   
    command = "az storage queue generate-sas " + params
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

def stats(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, timeout=None):
    params = get_params(locals())   
    command = "az storage queue stats " + params
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

def exists(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, timeout=None):
    params = get_params(locals())   
    command = "az storage queue exists " + params
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

def list(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, timeout=None, include_metadata=None, marker=None, num_results=None, prefix=None, show_next_marker=None):
    params = get_params(locals())   
    command = "az storage queue list " + params
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
