import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(account_name=None, account_key=None, connection_string=None, sas_token=None, share_name, path=None, timeout=None, exclude_dir=None, snapshot=None, num_results=None, marker=None):
    params = get_params(locals())   
    command = "az storage file list " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, path, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, timeout=None):
    params = get_params(locals())   
    command = "az storage file delete " + params
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

def resize(account_name=None, account_key=None, connection_string=None, sas_token=None, path, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, size, timeout=None):
    params = get_params(locals())   
    command = "az storage file resize " + params
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

def url(account_name=None, account_key=None, connection_string=None, sas_token=None, path, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, protocol=None):
    params = get_params(locals())   
    command = "az storage file url " + params
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

def generate_sas(account_name=None, account_key=None, connection_string=None, __SAS_TOKEN=None, path, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, permissions=None, expiry=None, start=None, policy_name=None, ip=None, https_only=None, cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None):
    params = get_params(locals())   
    command = "az storage file generate-sas " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, path, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, timeout=None, snapshot=None):
    params = get_params(locals())   
    command = "az storage file show " + params
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

def update(account_name=None, account_key=None, connection_string=None, sas_token=None, path, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, clear_content_settings=None, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, __CONTENT_SETTINGS=None, timeout=None):
    params = get_params(locals())   
    command = "az storage file update " + params
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

def exists(account_name=None, account_key=None, connection_string=None, sas_token=None, path, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, timeout=None, snapshot=None):
    params = get_params(locals())   
    command = "az storage file exists " + params
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

def download(account_name=None, account_key=None, connection_string=None, sas_token=None, path, no_progress=None, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, dest=None, open_mode=None, start_range=None, end_range=None, validate_content=None, __PROGRESS_CALLBACK=None, max_connections=None, timeout=None, snapshot=None):
    params = get_params(locals())   
    command = "az storage file download " + params
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

def upload(account_name=None, account_key=None, connection_string=None, sas_token=None, path=None, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, no_progress=None, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, source, __CONTENT_SETTINGS=None, metadata=None, validate_content=None, __PROGRESS_CALLBACK=None, max_connections=None, timeout=None):
    params = get_params(locals())   
    command = "az storage file upload " + params
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

def upload_batch(account_name=None, account_key=None, connection_string=None, sas_token=None, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, no_progress=None, destination, source, destination_path=None, pattern=None, dryrun=None, validate_content=None, __CONTENT_SETTINGS=None, max_connections=None, metadata=None, __PROGRESS_CALLBACK=None):
    params = get_params(locals())   
    command = "az storage file upload-batch " + params
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

def download_batch(account_name=None, account_key=None, connection_string=None, sas_token=None, no_progress=None, source, destination, pattern=None, dryrun=None, validate_content=None, max_connections=None, __PROGRESS_CALLBACK=None, snapshot=None):
    params = get_params(locals())   
    command = "az storage file download-batch " + params
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

def delete_batch(account_name=None, account_key=None, connection_string=None, sas_token=None, source, pattern=None, dryrun=None, timeout=None):
    params = get_params(locals())   
    command = "az storage file delete-batch " + params
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
