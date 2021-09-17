import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, timeout=None, metadata=None, public_access=None):
    params = get_params(locals())   
    command = "az storage fs create " + params
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

def list(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, prefix=None, include_metadata=None):
    params = get_params(locals())   
    command = "az storage fs list " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, timeout=None):
    params = get_params(locals())   
    command = "az storage fs show " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, timeout=None, yes=None):
    params = get_params(locals())   
    command = "az storage fs delete " + params
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
    command = "az storage fs exists " + params
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

def generate_sas(account_name=None, account_key=None, connection_string=None, __SAS_TOKEN=None, auth_mode=None, name, permissions=None, expiry=None, start=None, policy_name=None, ip=None, https_only=None, cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, full_uri=None, as_user=None):
    params = get_params(locals())   
    command = "az storage fs generate-sas " + params
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
