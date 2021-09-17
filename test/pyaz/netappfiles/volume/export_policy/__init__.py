import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, account_name, pool_name, volume_name, allowed_clients, rule_index, unix_read_only, unix_read_write, cifs, nfsv3, nfsv41, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az netappfiles volume export-policy add " + params
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

def list(account_name, pool_name, volume_name, resource_group):
    params = get_params(locals())   
    command = "az netappfiles volume export-policy list " + params
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

def remove(resource_group, account_name, pool_name, volume_name, rule_index, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az netappfiles volume export-policy remove " + params
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
