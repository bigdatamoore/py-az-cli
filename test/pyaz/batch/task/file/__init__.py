import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def delete(job_id, task_id, file_path, recursive=None, yes=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch task file delete " + params
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

def download(job_id, task_id, file_path, start_range=None, end_range=None, if_modified_since=None, if_unmodified_since=None, destination, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch task file download " + params
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

def show(job_id, task_id, file_path, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch task file show " + params
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

def list(job_id, task_id, recursive=None, filter=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch task file list " + params
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
