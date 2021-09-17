import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def acquire(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, tags_condition=None, blob_name, container_name, timeout=None, proposed_lease_id=None, lease_duration=None):
    params = get_params(locals())   
    command = "az storage blob lease acquire " + params
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

def break_(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, tags_condition=None, blob_name, container_name, timeout=None, lease_break_period=None):
    params = get_params(locals())   
    command = "az storage blob lease break " + params
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

def change(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, tags_condition=None, blob_name, container_name, timeout=None, proposed_lease_id, lease_id):
    params = get_params(locals())   
    command = "az storage blob lease change " + params
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

def renew(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, tags_condition=None, blob_name, container_name, timeout=None, lease_id):
    params = get_params(locals())   
    command = "az storage blob lease renew " + params
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

def release(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, tags_condition=None, blob_name, container_name, timeout=None, lease_id):
    params = get_params(locals())   
    command = "az storage blob lease release " + params
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
