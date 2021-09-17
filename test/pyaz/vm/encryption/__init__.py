import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def enable(resource_group, name, disk_encryption_keyvault, aad_client_id=None, aad_client_secret=None, aad_client_cert_thumbprint=None, key_encryption_keyvault=None, key_encryption_key=None, key_encryption_algorithm=None, volume_type=None, encrypt_format_all=None, force=None):
    params = get_params(locals())   
    command = "az vm encryption enable " + params
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

def disable(resource_group, name, volume_type=None, force=None):
    params = get_params(locals())   
    command = "az vm encryption disable " + params
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

def show(resource_group, name):
    params = get_params(locals())   
    command = "az vm encryption show " + params
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
