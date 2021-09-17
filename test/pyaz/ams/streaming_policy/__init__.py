import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, account_name, name, no_encryption_protocols=None, default_content_key_policy_name=None, cbcs_clear_tracks=None, cbcs_default_key_label=None, cbcs_default_key_policy_name=None, cbcs_key_to_track_mappings=None, cbcs_protocols=None, cbcs_play_ready_template=None, cbcs_play_ready_attributes=None, cbcs_widevine_template=None, cbcs_fair_play_template=None, cbcs_fair_play_allow_persistent_license=None, cenc_default_key_label=None, cenc_default_key_policy_name=None, cenc_clear_tracks=None, cenc_key_to_track_mappings=None, cenc_disable_play_ready=None, cenc_play_ready_template=None, cenc_play_ready_attributes=None, cenc_disable_widevine=None, cenc_widevine_template=None, cenc_protocols=None, envelope_clear_tracks=None, envelope_default_key_label=None, envelope_default_key_policy_name=None, envelope_key_to_track_mappings=None, envelope_protocols=None, envelope_template=None):
    params = get_params(locals())   
    command = "az ams streaming-policy create " + params
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
    command = "az ams streaming-policy list " + params
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

def show(resource_group, account_name, name):
    params = get_params(locals())   
    command = "az ams streaming-policy show " + params
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
    command = "az ams streaming-policy delete " + params
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
