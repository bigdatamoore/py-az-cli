import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def query(account_name=None, account_key=None, connection_string=None, sas_token=None, table_name, filter=None, select=None, num_results=None, marker=None, accept=None, __PROPERTY_RESOLVER=None, timeout=None):
    params = get_params(locals())   
    command = "az storage entity query " + params
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

def replace(account_name=None, account_key=None, connection_string=None, sas_token=None, table_name, entity, if_match=None, timeout=None):
    params = get_params(locals())   
    command = "az storage entity replace " + params
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

def merge(account_name=None, account_key=None, connection_string=None, sas_token=None, table_name, entity, if_match=None, timeout=None):
    params = get_params(locals())   
    command = "az storage entity merge " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, table_name, partition_key, row_key, if_match=None, timeout=None):
    params = get_params(locals())   
    command = "az storage entity delete " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, table_name, partition_key, row_key, select=None, accept=None, __PROPERTY_RESOLVER=None, timeout=None):
    params = get_params(locals())   
    command = "az storage entity show " + params
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

def insert(account_name=None, account_key=None, connection_string=None, sas_token=None, table_name, entity, if_exists=None, timeout=None):
    params = get_params(locals())   
    command = "az storage entity insert " + params
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
