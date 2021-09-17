import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(name, resource_group):
    params = get_params(locals())   
    command = "az backup vault backup-properties show " + params
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

def set(name, resource_group, backup_storage_redundancy=None, soft_delete_feature_state=None, cross_region_restore_flag=None):
    params = get_params(locals())   
    command = "az backup vault backup-properties set " + params
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
