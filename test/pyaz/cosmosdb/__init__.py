import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def show(resource_group, name):
    params = get_params(locals())   
    command = "az cosmosdb show " + params
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

def list_keys(resource_group, name):
    params = get_params(locals())   
    command = "az cosmosdb list-keys " + params
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

def list_read_only_keys(resource_group, name):
    params = get_params(locals())   
    command = "az cosmosdb list-read-only-keys " + params
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

def list_connection_strings(resource_group, name):
    params = get_params(locals())   
    command = "az cosmosdb list-connection-strings " + params
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

def regenerate_key(resource_group, name, key_kind):
    params = get_params(locals())   
    command = "az cosmosdb regenerate-key " + params
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

def check_name_exists(name):
    params = get_params(locals())   
    command = "az cosmosdb check-name-exists " + params
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

def delete(resource_group, name, yes=None):
    params = get_params(locals())   
    command = "az cosmosdb delete " + params
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

def failover_priority_change(resource_group, name, failover_policies):
    params = get_params(locals())   
    command = "az cosmosdb failover-priority-change " + params
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

def create(resource_group, name, locations=None, tags=None, kind=None, default_consistency_level=None, max_staleness_prefix=None, max_interval=None, ip_range_filter=None, enable_automatic_failover=None, capabilities=None, enable_virtual_network=None, virtual_network_rules=None, enable_multiple_write_locations=None, disable_key_based_metadata_write_access=None, key_uri=None, enable_public_network=None, enable_analytical_storage=None, enable_free_tier=None, server_version=None, network_acl_bypass=None, network_acl_bypass_resource_ids=None, backup_interval=None, backup_retention=None, assign_identity=None, default_identity=None, analytical_storage_schema_type=None, backup_policy_type=None, databases_to_restore=None, is_restore_request=None, restore_source=None, restore_timestamp=None):
    params = get_params(locals())   
    command = "az cosmosdb create " + params
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

def update(resource_group, name, locations=None, tags=None, default_consistency_level=None, max_staleness_prefix=None, max_interval=None, ip_range_filter=None, enable_automatic_failover=None, capabilities=None, enable_virtual_network=None, virtual_network_rules=None, enable_multiple_write_locations=None, disable_key_based_metadata_write_access=None, enable_public_network=None, enable_analytical_storage=None, network_acl_bypass=None, network_acl_bypass_resource_ids=None, server_version=None, backup_interval=None, backup_retention=None, default_identity=None, analytical_storage_schema_type=None, backup_policy_type=None):
    params = get_params(locals())   
    command = "az cosmosdb update " + params
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
    command = "az cosmosdb list " + params
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

def restore(resource_group, account_name, target_database_account_name, restore_timestamp, location, databases_to_restore=None):
    params = get_params(locals())   
    command = "az cosmosdb restore " + params
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
