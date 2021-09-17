import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def add(account_name=None, account_key=None, connection_string=None, sas_token=None, services, origins, methods, max_age=None, exposed_headers=None, allowed_headers=None, timeout=None):
    params = get_params(locals())   
    command = "az storage cors add " + params
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

def clear(account_name=None, account_key=None, connection_string=None, sas_token=None, services, timeout=None):
    params = get_params(locals())   
    command = "az storage cors clear " + params
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

def list(account_name=None, account_key=None, connection_string=None, sas_token=None, services=None, timeout=None):
    params = get_params(locals())   
    command = "az storage cors list " + params
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
