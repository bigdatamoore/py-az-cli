import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def start(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, source_sas=None, source_container=None, source_blob=None, source_snapshot=None, source_account_name=None, source_account_key=None, destination_container, destination_blob, source_uri=None, metadata=None, destination_if_modified_since=None, destination_if_unmodified_since=None, destination_if_match=None, destination_if_none_match=None, destination_lease_id=None, source_lease_id=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob incremental-copy start " + params
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

def cancel(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, name, copy_id, lease_id=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob incremental-copy cancel " + params
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
