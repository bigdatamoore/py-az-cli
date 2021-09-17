import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_group=None, account_name):
    params = get_params(locals())   
    command = "az storage account file-service-properties show " + params
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

def update(resource_group=None, account_name, enable_delete_retention=None, delete_retention_days=None, enable_smb_multichannel=None, versions=None, auth_methods=None, kerb_ticket_encryption=None, channel_encryption=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az storage account file-service-properties update " + params
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
