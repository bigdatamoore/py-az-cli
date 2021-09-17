import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def init_recovery(id=None, hsm_name=None, sd_exchange_key, __VAULT_BASE_URL=None):
    params = get_params(locals())   
    command = "az keyvault security-domain init-recovery " + params
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

def upload(id=None, hsm_name=None, sd_file, sd_exchange_key, sd_wrapping_keys, passwords=None, __VAULT_BASE_URL=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault security-domain upload " + params
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

def download(id=None, hsm_name=None, sd_wrapping_keys, security_domain_file, sd_quorum, __VAULT_BASE_URL=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault security-domain download " + params
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

def wait(hsm_name=None, target_operation=None, id=None, __VAULT_BASE_URL=None):
    params = get_params(locals())   
    command = "az keyvault security-domain wait " + params
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
