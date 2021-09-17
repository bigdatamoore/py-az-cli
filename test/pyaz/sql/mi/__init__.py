import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(admin_user=None, admin_password=None, license_type=None, minimal_tls_version=None, subnet, capacity=None, storage=None, collation=None, proxy_override=None, public_data_endpoint_enabled=None, timezone_id=None, tags=None, backup_storage_redundancy=None, yes=None, maint_config_id=None, primary_user_assigned_identity_id=None, key_id=None, family=None, __NAME=None, tier=None, vnet_name=None, name, resource_group, location=None, assign_identity=None, __SKU=None, user_assigned_identity_id=None, identity_type=None, enable_ad_only_auth=None, external_admin_principal_type=None, external_admin_sid=None, external_admin_name=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql mi create " + params
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

def delete(resource_group, name, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql mi delete " + params
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

def show(resource_group, name, expand_ad_admin=None):
    params = get_params(locals())   
    command = "az sql mi show " + params
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

def list(resource_group=None, expand_ad_admin=None):
    params = get_params(locals())   
    command = "az sql mi list " + params
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

def update(admin_password=None, tags=None, family=None, __NAME=None, tier=None, vnet_name=None, resource_group, name, license_type=None, capacity=None, storage=None, assign_identity=None, proxy_override=None, public_data_endpoint_enabled=None, minimal_tls_version=None, maint_config_id=None, primary_user_assigned_identity_id=None, key_id=None, identity_type=None, user_assigned_identity_id=None, subnet=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql mi update " + params
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

def failover(resource_group, name, replica_type=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql mi failover " + params
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
