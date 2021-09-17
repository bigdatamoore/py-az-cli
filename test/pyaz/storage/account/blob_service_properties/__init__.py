import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_group=None, account_name):
    params = get_params(locals())   
    command = "az storage account blob-service-properties show " + params
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

def update(resource_group=None, account_name, enable_change_feed=None, change_feed_retention_days=None, enable_delete_retention=None, delete_retention_days=None, enable_restore_policy=None, restore_days=None, enable_versioning=None, enable_container_delete_retention=None, container_delete_retention_days=None, default_service_version=None, enable_last_access_tracking=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az storage account blob-service-properties update " + params
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
