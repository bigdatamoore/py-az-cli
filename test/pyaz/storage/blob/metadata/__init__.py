import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, name, snapshot=None, lease_id=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob metadata show " + params
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

def update(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, name, metadata=None, lease_id=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob metadata update " + params
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
