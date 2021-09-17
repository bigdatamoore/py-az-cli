import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, account_name, name, policy_option_name, description=None, clear_key_configuration=None, open_restriction=None, issuer=None, audience=None, token_key=None, token_key_type=None, alt_symmetric_token_keys=None, alt_rsa_token_keys=None, alt_x509_token_keys=None, token_claims=None, token_type=None, open_id_connect_discovery_document=None, widevine_template=None, ask=None, fair_play_pfx_password=None, fair_play_pfx=None, rental_and_lease_key_type=None, rental_duration=None, play_ready_template=None, fp_playback_duration_seconds=None, fp_storage_duration_seconds=None):
    params = get_params(locals())   
    command = "az ams content-key-policy create " + params
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

def show(resource_group, account_name, name, with_secrets=None):
    params = get_params(locals())   
    command = "az ams content-key-policy show " + params
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

def delete(resource_group, account_name, name):
    params = get_params(locals())   
    command = "az ams content-key-policy delete " + params
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

def list(resource_group, account_name, filter=None, top=None, orderby=None):
    params = get_params(locals())   
    command = "az ams content-key-policy list " + params
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

def update(resource_group, account_name, name, description=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az ams content-key-policy update " + params
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
