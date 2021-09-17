import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, permissions=None, umask=None, __CONTENT_SETTINGS=None, metadata=None):
    params = get_params(locals())   
    command = "az storage fs file create " + params
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

def upload(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, source, overwrite=None, __CONTENT_SETTINGS=None, metadata=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, umask=None, permissions=None):
    params = get_params(locals())   
    command = "az storage fs file upload " + params
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

def exists(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None):
    params = get_params(locals())   
    command = "az storage fs file exists " + params
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

def append(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None, content):
    params = get_params(locals())   
    command = "az storage fs file append " + params
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

def download(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None, destination=None, overwrite=None):
    params = get_params(locals())   
    command = "az storage fs file download " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None):
    params = get_params(locals())   
    command = "az storage fs file show " + params
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

def list(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, path=None, recursive=None, num_results=None, timeout=None, exclude_dir=None, marker=None, show_next_marker=None):
    params = get_params(locals())   
    command = "az storage fs file list " + params
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

def move(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, _f, _p, new_path):
    params = get_params(locals())   
    command = "az storage fs file move " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, _f, _p, timeout=None, yes=None):
    params = get_params(locals())   
    command = "az storage fs file delete " + params
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
