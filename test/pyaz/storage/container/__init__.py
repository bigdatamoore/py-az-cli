import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, timeout=None, include_metadata=None, include_deleted=None, marker=None, num_results=None, prefix=None, show_next_marker=None):
    params = get_params(locals())   
    command = "az storage container list " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, fail_not_exist=None, lease_id=None, if_modified_since=None, if_unmodified_since=None, timeout=None, bypass_immutability_policy=None, __PROCESSED_RESOURCE_GROUP=None, __PROCESSED_ACCOUNT_NAME=None, __MGMT_CLIENT=None):
    params = get_params(locals())   
    command = "az storage container delete " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, lease_id=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container show " + params
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

def create(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, resource_group=None, metadata=None, public_access=None, fail_on_exist=None, timeout=None, default_encryption_scope=None, prevent_encryption_scope_override=None):
    params = get_params(locals())   
    command = "az storage container create " + params
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

def generate_sas(account_name=None, account_key=None, connection_string=None, __SAS_TOKEN=None, auth_mode=None, name, permissions=None, expiry=None, start=None, policy_name=None, ip=None, https_only=None, cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, as_user=None):
    params = get_params(locals())   
    command = "az storage container generate-sas " + params
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

def exists(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, __BLOB_NAME=None, __SNAPSHOT=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container exists " + params
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

def set_permission(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, __SIGNED_IDENTIFIERS=None, public_access=None, lease_id=None, if_modified_since=None, if_unmodified_since=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container set-permission " + params
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

def show_permission(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, lease_id=None, timeout=None):
    params = get_params(locals())   
    command = "az storage container show-permission " + params
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

def restore(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, timeout=None, name, deleted_version):
    params = get_params(locals())   
    command = "az storage container restore " + params
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
