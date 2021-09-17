import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, account_name, name, policy_option_name, clear_key_configuration=None, open_restriction=None, issuer=None, audience=None, token_key=None, token_key_type=None, alt_symmetric_token_keys=None, alt_rsa_token_keys=None, alt_x509_token_keys=None, token_claims=None, token_type=None, open_id_connect_discovery_document=None, widevine_template=None, ask=None, fair_play_pfx_password=None, fair_play_pfx=None, rental_and_lease_key_type=None, rental_duration=None, play_ready_template=None, fp_playback_duration_seconds=None, fp_storage_duration_seconds=None):
    params = get_params(locals())   
    command = "az ams content-key-policy option add " + params
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

def remove(resource_group, account_name, name, policy_option_id):
    params = get_params(locals())   
    command = "az ams content-key-policy option remove " + params
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

def update(resource_group, account_name, name, policy_option_id, policy_option_name=None, issuer=None, audience=None, token_key=None, token_key_type=None, add_alt_token_key=None, add_alt_token_key_type=None, token_claims=None, token_type=None, open_id_connect_discovery_document=None, widevine_template=None, ask=None, fair_play_pfx_password=None, fair_play_pfx=None, rental_and_lease_key_type=None, rental_duration=None, play_ready_template=None, fp_playback_duration_seconds=None, fp_storage_duration_seconds=None):
    params = get_params(locals())   
    command = "az ams content-key-policy option update " + params
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
