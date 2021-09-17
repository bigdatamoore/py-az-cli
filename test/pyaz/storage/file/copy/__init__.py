import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def start(account_name=None, account_key=None, connection_string=None, sas_token=None, destination_path, source_sas=None, source_container=None, source_blob=None, source_snapshot=None, source_account_name=None, source_account_key=None, source_path=None, source_share=None, file_snapshot=None, destination_share, __DIRECTORY_NAME=None, __FILE_NAME=None, source_uri=None, metadata=None, timeout=None):
    params = get_params(locals())   
    command = "az storage file copy start " + params
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

def cancel(account_name=None, account_key=None, connection_string=None, sas_token=None, destination_path, destination_share, __DIRECTORY_NAME=None, __FILE_NAME=None, copy_id, timeout=None):
    params = get_params(locals())   
    command = "az storage file copy cancel " + params
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

def start_batch(account_name=None, account_key=None, connection_string=None, sas_token=None, source_account_name=None, source_account_key=None, source_uri=None, source_client=None, destination_share=None, destination_path=None, source_container=None, source_share=None, source_sas=None, pattern=None, dryrun=None, metadata=None, timeout=None):
    params = get_params(locals())   
    command = "az storage file copy start-batch " + params
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
