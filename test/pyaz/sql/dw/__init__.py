import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(__CATALOG_COLLATION=None, collation=None, __ELASTIC_POOL_ID=None, __LICENSE_TYPE=None, max_size=None, service_objective=None, __RESTORE_POINT_IN_TIME=None, __SAMPLE_NAME=None, __SKU=None, __SOURCE_DATABASE_DELETION_DATE=None, tags=None, zone_redundant=None, __AUTO_PAUSE_DELAY=None, __MIN_CAPACITY=None, __COMPUTE_MODEL=None, __READ_SCALE=None, __HIGH_AVAILABILITY_REPLICA_COUNT=None, backup_storage_redundancy=None, __MAINTENANCE_CONFIGURATION_ID=None, __IS_LEDGER_ON=None, __CAPACITY=None, __FAMILY=None, __TIER=None, name, server, resource_group, no_wait=None):
    params = get_params(locals())   
    command = "az sql dw create " + params
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
    command = "az sql dw show " + params
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

def list(server, resource_group):
    params = get_params(locals())   
    command = "az sql dw list " + params
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
    command = "az sql dw delete " + params
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

def pause(name, server, resource_group):
    params = get_params(locals())   
    command = "az sql dw pause " + params
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

def resume(name, server, resource_group):
    params = get_params(locals())   
    command = "az sql dw resume " + params
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

def update(resource_group, server, name, max_size=None, service_objective=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az sql dw update " + params
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
