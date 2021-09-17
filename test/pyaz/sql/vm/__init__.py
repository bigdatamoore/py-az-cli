import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def update(resource_group, name, license_type=None, image_sku=None, enable_auto_patching=None, day_of_week=None, maintenance_window_start_hour=None, maintenance_window_duration=None, enable_auto_backup=None, enable_encryption=None, retention_period=None, storage_account=None, yes=None, sa_key=None, backup_pwd=None, backup_system_dbs=None, backup_schedule_type=None, sql_mgmt_type=None, full_backup_frequency=None, full_backup_start_hour=None, full_backup_duration=None, log_backup_frequency=None, enable_key_vault_credential=None, credential_name=None, key_vault=None, sp_name=None, sp_secret=None, connectivity_type=None, port=None, sql_workload_type=None, enable_r_services=None, tags=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az sql vm update " + params
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

def show(resource_group, name, expand=None):
    params = get_params(locals())   
    command = "az sql vm show " + params
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
    command = "az sql vm list " + params
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

def add_to_group(name, resource_group, sqlvm_group, service_acc_pwd=None, operator_acc_pwd=None, _b=None):
    params = get_params(locals())   
    command = "az sql vm add-to-group " + params
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

def remove_from_group(name, resource_group):
    params = get_params(locals())   
    command = "az sql vm remove-from-group " + params
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
    command = "az sql vm delete " + params
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

def create(name, resource_group, license_type=None, location=None, image_sku=None, enable_auto_patching=None, sql_mgmt_type=None, day_of_week=None, maintenance_window_start_hour=None, maintenance_window_duration=None, enable_auto_backup=None, enable_encryption=None, retention_period=None, storage_account=None, sa_key=None, backup_pwd=None, backup_system_dbs=None, backup_schedule_type=None, full_backup_frequency=None, full_backup_start_hour=None, full_backup_duration=None, log_backup_frequency=None, enable_key_vault_credential=None, credential_name=None, key_vault=None, sp_name=None, sp_secret=None, connectivity_type=None, port=None, sql_auth_update_username=None, sql_auth_update_pwd=None, sql_workload_type=None, enable_r_services=None, tags=None, image_offer=None):
    params = get_params(locals())   
    command = "az sql vm create " + params
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
