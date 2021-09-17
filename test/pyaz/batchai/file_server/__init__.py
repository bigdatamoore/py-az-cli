import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, workspace, name, config_file=None, vm_size=None, user_name=None, ssh_key=None, password=None, generate_ssh_keys=None, disk_count=None, disk_size=None, caching_type=None, storage_sku=None, subnet=None, no_wait=None):
    params = get_params(locals())   
    command = "az batchai file-server create " + params
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

def list(resource_group, workspace, __FILE_SERVERS_LIST_BY_WORKSPACE_OPTIONS=None):
    params = get_params(locals())   
    command = "az batchai file-server list " + params
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
