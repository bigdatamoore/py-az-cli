import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, name, username, password, domain, dns, smb_server_name, organizational_unit=None, kdc_ip=None, ad_name=None, server_root_ca_cert=None, backup_operators=None, aes_encryption=None, ldap_signing=None, security_operators=None, ldap_over_tls=None, allow_local_ldap_users=None, tags=None, administrators=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az netappfiles account ad add " + params
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

def list(name, resource_group):
    params = get_params(locals())   
    command = "az netappfiles account ad list " + params
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

def remove(name, resource_group, active_directory):
    params = get_params(locals())   
    command = "az netappfiles account ad remove " + params
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
