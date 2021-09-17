import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(id=None, hsm_name=None, include_managed=None, vault_name=None, maxresults=None):
    params = get_params(locals())   
    command = "az keyvault key list " + params
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

def list_versions(id=None, hsm_name=None, vault_name=None, name=None, maxresults=None):
    params = get_params(locals())   
    command = "az keyvault key list-versions " + params
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

def list_deleted(id=None, hsm_name=None, vault_name=None, maxresults=None):
    params = get_params(locals())   
    command = "az keyvault key list-deleted " + params
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

def create(name=None, vault_name=None, hsm_name=None, protection=None, id=None, size=None, ops=None, disabled=None, expires=None, not_before=None, tags=None, kty=None, curve=None):
    params = get_params(locals())   
    command = "az keyvault key create " + params
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

def set_attributes(id=None, hsm_name=None, enabled=None, expires=None, not_before=None, vault_name=None, name=None, version=None, ops=None, key_attributes=None, tags=None):
    params = get_params(locals())   
    command = "az keyvault key set-attributes " + params
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

def show(id=None, hsm_name=None, vault_name=None, name=None, version=None):
    params = get_params(locals())   
    command = "az keyvault key show " + params
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

def show_deleted(id=None, hsm_name=None, vault_name=None, name=None):
    params = get_params(locals())   
    command = "az keyvault key show-deleted " + params
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

def delete(id=None, hsm_name=None, vault_name=None, name=None):
    params = get_params(locals())   
    command = "az keyvault key delete " + params
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

def purge(id=None, hsm_name=None, vault_name=None, name=None):
    params = get_params(locals())   
    command = "az keyvault key purge " + params
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

def recover(id=None, hsm_name=None, vault_name=None, name=None):
    params = get_params(locals())   
    command = "az keyvault key recover " + params
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

def backup(id=None, file, vault_name=None, name=None, hsm_name=None):
    params = get_params(locals())   
    command = "az keyvault key backup " + params
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

def restore(file=None, vault_name=None, hsm_name=None, id=None, storage_resource_uri=None, storage_account_name=None, blob_container_name=None, storage_container_SAS_token=None, backup_folder=None, name=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault key restore " + params
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

def import_(name=None, vault_name=None, hsm_name=None, id=None, protection=None, ops=None, disabled=None, expires=None, not_before=None, tags=None, pem_file=None, pem_string=None, pem_password=None, byok_file=None, byok_string=None, kty=None, curve=None):
    params = get_params(locals())   
    command = "az keyvault key import " + params
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

def download(id=None, file, hsm_name=None, vault_name=None, name=None, version=None, encoding=None):
    params = get_params(locals())   
    command = "az keyvault key download " + params
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

def get_policy_template():
    params = get_params(locals())   
    command = "az keyvault key get-policy-template " + params
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

def encrypt(id=None, hsm_name=None, data_type=None, vault_name=None, name=None, version=None, algorithm, value):
    params = get_params(locals())   
    command = "az keyvault key encrypt " + params
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

def decrypt(id=None, hsm_name=None, data_type=None, vault_name=None, name=None, version=None, algorithm, value):
    params = get_params(locals())   
    command = "az keyvault key decrypt " + params
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
