import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def check_name(name):
    params = get_params(locals())   
    command = "az storage account check-name " + params
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

def create(resource_group, name, sku=None, location=None, kind=None, tags=None, custom_domain=None, encryption_services=None, encryption_key_source=None, encryption_key_name=None, encryption_key_vault=None, encryption_key_version=None, access_tier=None, https_only=None, enable_files_aadds=None, bypass=None, default_action=None, assign_identity=None, enable_large_file_share=None, enable_files_adds=None, domain_name=None, net_bios_domain_name=None, forest_name=None, domain_guid=None, domain_sid=None, azure_storage_sid=None, enable_hierarchical_namespace=None, encryption_key_type_for_table=None, encryption_key_type_for_queue=None, routing_choice=None, publish_microsoft_endpoints=None, publish_internet_endpoints=None, require_infrastructure_encryption=None, allow_blob_public_access=None, min_tls_version=None, allow_shared_key_access=None, edge_zone=None, identity_type=None, user_identity_id=None, key_vault_user_identity_id=None, sas_expiration_period=None, key_expiration_period_in_days=None, allow_cross_tenant_replication=None, default_share_permission=None, enable_nfs_v3=None, subnet=None, vnet_name=None, action=None):
    params = get_params(locals())   
    command = "az storage account create " + params
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

def delete(resource_group=None, name, yes=None):
    params = get_params(locals())   
    command = "az storage account delete " + params
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

def show(resource_group=None, name, expand=None):
    params = get_params(locals())   
    command = "az storage account show " + params
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

def list(resource_group=None):
    params = get_params(locals())   
    command = "az storage account list " + params
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

def show_usage(location):
    params = get_params(locals())   
    command = "az storage account show-usage " + params
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

def show_connection_string(resource_group=None, name, protocol=None, blob_endpoint=None, file_endpoint=None, queue_endpoint=None, table_endpoint=None, sas_token=None, key=None):
    params = get_params(locals())   
    command = "az storage account show-connection-string " + params
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

def update(resource_group=None, name, sku=None, tags=None, custom_domain=None, use_subdomain=None, encryption_services=None, encryption_key_source=None, encryption_key_version=None, encryption_key_name=None, encryption_key_vault=None, access_tier=None, https_only=None, enable_files_aadds=None, assign_identity=None, bypass=None, default_action=None, enable_large_file_share=None, enable_files_adds=None, domain_name=None, net_bios_domain_name=None, forest_name=None, domain_guid=None, domain_sid=None, azure_storage_sid=None, routing_choice=None, publish_microsoft_endpoints=None, publish_internet_endpoints=None, allow_blob_public_access=None, min_tls_version=None, allow_shared_key_access=None, identity_type=None, user_identity_id=None, key_vault_user_identity_id=None, sas_expiration_period=None, key_expiration_period_in_days=None, allow_cross_tenant_replication=None, default_share_permission=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az storage account update " + params
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

def failover(resource_group=None, name, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az storage account failover " + params
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

def revoke_delegation_keys(resource_group=None, name):
    params = get_params(locals())   
    command = "az storage account revoke-delegation-keys " + params
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

def generate_sas(account_name=None, account_key=None, connection_string=None, __SAS_TOKEN=None, services, resource_types, permissions, expiry, start=None, ip=None, https_only=None):
    params = get_params(locals())   
    command = "az storage account generate-sas " + params
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
