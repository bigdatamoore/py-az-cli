import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def mount_rp(resource_group, vault_name, container_name, item_name, rp_name):
    params = get_params(locals())   
    command = "az backup restore files mount-rp " + params
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

def unmount_rp(resource_group, vault_name, container_name, item_name, rp_name):
    params = get_params(locals())   
    command = "az backup restore files unmount-rp " + params
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
