import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(account_name=None, account_key=None, connection_string=None, sas_token=None, prefix=None, marker=None, num_results=None, include_metadata=None, timeout=None, include_snapshots=None):
    params = get_params(locals())   
    command = "az storage share list " + params
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

def create(account_name=None, account_key=None, connection_string=None, sas_token=None, name, metadata=None, quota=None, fail_on_exist=None, timeout=None):
    params = get_params(locals())   
    command = "az storage share create " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, name, fail_not_exist=None, timeout=None, snapshot=None, delete_snapshots=None):
    params = get_params(locals())   
    command = "az storage share delete " + params
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

def generate_sas(account_name=None, account_key=None, connection_string=None, __SAS_TOKEN=None, name, permissions=None, expiry=None, start=None, policy_name=None, ip=None, https_only=None, cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None):
    params = get_params(locals())   
    command = "az storage share generate-sas " + params
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

def stats(account_name=None, account_key=None, connection_string=None, sas_token=None, name, timeout=None):
    params = get_params(locals())   
    command = "az storage share stats " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, name, timeout=None, snapshot=None):
    params = get_params(locals())   
    command = "az storage share show " + params
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

def update(account_name=None, account_key=None, connection_string=None, sas_token=None, name, quota, timeout=None):
    params = get_params(locals())   
    command = "az storage share update " + params
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

def snapshot(account_name=None, account_key=None, connection_string=None, sas_token=None, name, metadata=None, quota=None, timeout=None):
    params = get_params(locals())   
    command = "az storage share snapshot " + params
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

def exists(account_name=None, account_key=None, connection_string=None, sas_token=None, name, __DIRECTORY_NAME=None, __FILE_NAME=None, timeout=None, snapshot=None):
    params = get_params(locals())   
    command = "az storage share exists " + params
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

def url(account_name=None, account_key=None, connection_string=None, sas_token=None, name, unc=None, protocol=None):
    params = get_params(locals())   
    command = "az storage share url " + params
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
