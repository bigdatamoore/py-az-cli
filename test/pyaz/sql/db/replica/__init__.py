import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(__CATALOG_COLLATION=None, __COLLATION=None, elastic_pool=None, license_type=None, __MAX_SIZE_BYTES=None, service_objective=None, __RESTORE_POINT_IN_TIME=None, __SAMPLE_NAME=None, __SKU=None, __SOURCE_DATABASE_DELETION_DATE=None, tags=None, zone_redundant=None, auto_pause_delay=None, min_capacity=None, compute_model=None, read_scale=None, read_replicas=None, backup_storage_redundancy=None, __MAINTENANCE_CONFIGURATION_ID=None, __IS_LEDGER_ON=None, capacity=None, family=None, __TIER=None, name, server, resource_group, partner_server, partner_database=None, partner_resource_group=None, secondary_type=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql db replica create " + params
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

def list_links(resource_group, server, name):
    params = get_params(locals())   
    command = "az sql db replica list-links " + params
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

def delete_link(name, server, resource_group, partner_server, partner_resource_group=None, yes=None):
    params = get_params(locals())   
    command = "az sql db replica delete-link " + params
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

def set_primary(name, server, resource_group, allow_data_loss=None):
    params = get_params(locals())   
    command = "az sql db replica set-primary " + params
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
