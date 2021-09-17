import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show_connection_string(client, name=None, server=None, auth_type=None):
    params = get_params(locals())   
    command = "az sql db show-connection-string " + params
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

def create(catalog_collation=None, collation=None, elastic_pool=None, license_type=None, max_size=None, service_objective=None, __RESTORE_POINT_IN_TIME=None, sample_name=None, __SKU=None, __SOURCE_DATABASE_DELETION_DATE=None, tags=None, zone_redundant=None, auto_pause_delay=None, min_capacity=None, compute_model=None, read_scale=None, read_replicas=None, backup_storage_redundancy=None, maint_config_id=None, ledger_on=None, capacity=None, family=None, tier=None, name, server, resource_group, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql db create " + params
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

def copy(__CATALOG_COLLATION=None, __COLLATION=None, elastic_pool=None, license_type=None, __MAX_SIZE_BYTES=None, service_objective=None, __RESTORE_POINT_IN_TIME=None, __SAMPLE_NAME=None, __SKU=None, __SOURCE_DATABASE_DELETION_DATE=None, tags=None, zone_redundant=None, auto_pause_delay=None, min_capacity=None, compute_model=None, read_scale=None, read_replicas=None, backup_storage_redundancy=None, __MAINTENANCE_CONFIGURATION_ID=None, __IS_LEDGER_ON=None, capacity=None, family=None, __TIER=None, name, server, resource_group, dest_name, dest_server=None, dest_resource_group=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql db copy " + params
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

def restore(__CATALOG_COLLATION=None, __COLLATION=None, elastic_pool=None, license_type=None, __MAX_SIZE_BYTES=None, service_objective=None, time=None, __SAMPLE_NAME=None, __SKU=None, deleted_time=None, tags=None, zone_redundant=None, auto_pause_delay=None, min_capacity=None, compute_model=None, read_scale=None, read_replicas=None, backup_storage_redundancy=None, __MAINTENANCE_CONFIGURATION_ID=None, __IS_LEDGER_ON=None, capacity=None, family=None, tier=None, name, server, resource_group, dest_name, no_wait=None):
    params = get_params(locals())   
    command = "az sql db restore " + params
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

def rename(name, server, resource_group, new_name):
    params = get_params(locals())   
    command = "az sql db rename " + params
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

def show(resource_group, server, name):
    params = get_params(locals())   
    command = "az sql db show " + params
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

def list(server, resource_group, elastic_pool=None):
    params = get_params(locals())   
    command = "az sql db list " + params
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

def delete(resource_group, server, name, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql db delete " + params
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

def update(resource_group, server, name, elastic_pool=None, max_size=None, service_objective=None, zone_redundant=None, tier=None, family=None, capacity=None, read_scale=None, read_replicas=None, min_capacity=None, auto_pause_delay=None, compute_model=None, backup_storage_redundancy=None, maint_config_id=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql db update " + params
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

def export(admin_user, admin_password, auth_type=None, storage_key, storage_key_type, storage_uri, name, server, resource_group):
    params = get_params(locals())   
    command = "az sql db export " + params
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

def import_(admin_user, admin_password, auth_type=None, storage_key, storage_key_type, storage_uri, name, server, resource_group):
    params = get_params(locals())   
    command = "az sql db import " + params
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

def list_editions(location, tier=None, service_objective=None, dtu=None, vcores=None, show_details=None, available=None):
    params = get_params(locals())   
    command = "az sql db list-editions " + params
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

def list_deleted(resource_group, server):
    params = get_params(locals())   
    command = "az sql db list-deleted " + params
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

def list_usages(resource_group, server, name):
    params = get_params(locals())   
    command = "az sql db list-usages " + params
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
