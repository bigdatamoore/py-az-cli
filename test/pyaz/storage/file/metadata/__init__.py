import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(account_name=None, account_key=None, connection_string=None, sas_token=None, path, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, timeout=None, snapshot=None):
    params = get_params(locals())   
    command = "az storage file metadata show " + params
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

def update(account_name=None, account_key=None, connection_string=None, sas_token=None, path, share_name, __DIRECTORY_NAME=None, __FILE_NAME=None, metadata=None, timeout=None):
    params = get_params(locals())   
    command = "az storage file metadata update " + params
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
