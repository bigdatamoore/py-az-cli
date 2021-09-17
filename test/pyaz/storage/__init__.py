import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def remove(account_name=None, account_key=None, connection_string=None, sas_token=None, __SERVICE=None, __TARGET=None, recursive=None, exclude_pattern=None, include_pattern=None, exclude_path=None, include_path=None, container_name=None, name=None, share_name=None, path=None):
    params = get_params(locals())   
    command = "az storage remove " + params
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

def copy(account_name=None, account_key=None, connection_string=None, sas_token=None, destination_container=None, destination_blob=None, destination_share=None, destination_file_path=None, source_container=None, source_blob=None, source_share=None, source_file_path=None, source_account_name=None, source_account_key=None, source_connection_string=None, source_sas=None, source=None, destination=None, put_md5=None, recursive=None, blob_type=None, preserve_s2s_access_tier=None, content_type=None, follow_symlinks=None, exclude_pattern=None, include_pattern=None, exclude_path=None, include_path=None, cap_mbps=None):
    params = get_params(locals())   
    command = "az storage copy " + params
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
