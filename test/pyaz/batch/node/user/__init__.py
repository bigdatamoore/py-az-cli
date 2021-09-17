import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(pool_id, node_id, name=None, is_admin=None, expiry_time=None, password=None, ssh_public_key=None, json_file=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node user create " + params
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

def delete(pool_id, node_id, user_name, yes=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node user delete " + params
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

def reset(pool_id, node_id, user_name, password=None, expiry_time=None, ssh_public_key=None, json_file=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node user reset " + params
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
