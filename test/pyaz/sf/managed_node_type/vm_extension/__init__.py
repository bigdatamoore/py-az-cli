import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, cluster_name, _n, extension_name, publisher, extension_type, type_handler_version, force_update_tag=None, auto_upgrade_minor_version=None, setting=None, protected_setting=None, provision_after_extension=None):
    params = get_params(locals())   
    command = "az sf managed-node-type vm-extension add " + params
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

def delete(resource_group, cluster_name, _n, extension_name):
    params = get_params(locals())   
    command = "az sf managed-node-type vm-extension delete " + params
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
