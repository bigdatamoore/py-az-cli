import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def restore_disks(resource_group, vault_name, container_name, item_name, rp_name, storage_account, target_resource_group=None, restore_to_staging_storage_account=None, restore_only_osdisk=None, diskslist=None, restore_as_unmanaged_disks=None, use_secondary_region=None, rehydration_duration=None, rehydration_priority=None, disk_encryption_set_id=None, mi_system_assigned=None, mi_user_assigned=None):
    params = get_params(locals())   
    command = "az backup restore restore-disks " + params
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

def restore_azurefileshare(resource_group, vault_name, rp_name, container_name, item_name, restore_mode, resolve_conflict, target_storage_account=None, target_file_share=None, target_folder=None):
    params = get_params(locals())   
    command = "az backup restore restore-azurefileshare " + params
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

def restore_azurefiles(resource_group, vault_name, rp_name, container_name, item_name, restore_mode, resolve_conflict, target_storage_account=None, target_file_share=None, target_folder=None, source_file_type=None, source_file_path=None):
    params = get_params(locals())   
    command = "az backup restore restore-azurefiles " + params
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

def restore_azurewl(resource_group, vault_name, recovery_config, rehydration_duration=None, rehydration_priority=None):
    params = get_params(locals())   
    command = "az backup restore restore-azurewl " + params
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
