import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def check_vm(vm_id=None, vm=None, resource_group=None):
    params = get_params(locals())   
    command = "az backup protection check-vm " + params
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

def enable_for_vm(resource_group, vault_name, vm, policy_name, diskslist=None, disk_list_setting=None, exclude_all_data_disks=None):
    params = get_params(locals())   
    command = "az backup protection enable-for-vm " + params
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

def update_for_vm(resource_group, vault_name, container_name, item_name, diskslist=None, disk_list_setting=None, exclude_all_data_disks=None):
    params = get_params(locals())   
    command = "az backup protection update-for-vm " + params
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

def backup_now(resource_group, vault_name, item_name, retain_until=None, container_name=None, backup_management_type=None, workload_type=None, backup_type=None, enable_compression=None):
    params = get_params(locals())   
    command = "az backup protection backup-now " + params
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

def disable(resource_group, vault_name, item_name, container_name, backup_management_type=None, workload_type=None, delete_backup_data=None, yes=None):
    params = get_params(locals())   
    command = "az backup protection disable " + params
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

def enable_for_azurefileshare(resource_group, vault_name, policy_name, storage_account, azure_file_share):
    params = get_params(locals())   
    command = "az backup protection enable-for-azurefileshare " + params
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

def enable_for_azurewl(resource_group, vault_name, policy_name, protectable_item_type, protectable_item_name, server_name, workload_type):
    params = get_params(locals())   
    command = "az backup protection enable-for-azurewl " + params
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

def auto_enable_for_azurewl(resource_group, vault_name, policy_name, protectable_item_name, protectable_item_type, server_name, workload_type):
    params = get_params(locals())   
    command = "az backup protection auto-enable-for-azurewl " + params
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

def auto_disable_for_azurewl(resource_group, vault_name, item_name):
    params = get_params(locals())   
    command = "az backup protection auto-disable-for-azurewl " + params
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

def resume(resource_group, vault_name, container_name, item_name, policy_name, workload_type=None, backup_management_type=None):
    params = get_params(locals())   
    command = "az backup protection resume " + params
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

def undelete(resource_group, vault_name, container_name, item_name, backup_management_type, workload_type=None):
    params = get_params(locals())   
    command = "az backup protection undelete " + params
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
