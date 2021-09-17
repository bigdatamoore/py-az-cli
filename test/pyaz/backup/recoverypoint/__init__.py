import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, vault_name, container_name, item_name, name, workload_type=None, backup_management_type=None, use_secondary_region=None):
    params = get_params(locals())   
    command = "az backup recoverypoint show " + params
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

def list(resource_group, vault_name, container_name, item_name, backup_management_type=None, workload_type=None, start_date=None, end_date=None, use_secondary_region=None, is_ready_for_move=None, target_tier=None, tier=None, recommended_for_archive=None):
    params = get_params(locals())   
    command = "az backup recoverypoint list " + params
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

def move(resource_group, vault_name, container_name, item_name, name, source_tier, destination_tier, backup_management_type=None, workload_type=None):
    params = get_params(locals())   
    command = "az backup recoverypoint move " + params
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

def show_log_chain(resource_group, vault_name, container_name, item_name, backup_management_type=None, workload_type=None, start_date=None, end_date=None, use_secondary_region=None):
    params = get_params(locals())   
    command = "az backup recoverypoint show-log-chain " + params
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
