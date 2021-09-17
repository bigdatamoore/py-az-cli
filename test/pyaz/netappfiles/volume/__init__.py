import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, account_name, pool_name, volume_name):
    params = get_params(locals())   
    command = "az netappfiles volume show " + params
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

def list(resource_group, account_name, pool_name):
    params = get_params(locals())   
    command = "az netappfiles volume list " + params
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

def delete(resource_group, account_name, pool_name, volume_name):
    params = get_params(locals())   
    command = "az netappfiles volume delete " + params
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

def create(account_name, pool_name, volume_name, resource_group, location, file_path, usage_threshold, vnet, subnet=None, service_level=None, protocol_types=None, volume_type=None, endpoint_type=None, replication_schedule=None, remote_volume_resource_id=None, tags=None, snapshot_id=None, snapshot_policy_id=None, backup_policy_id=None, backup_enabled=None, backup_id=None, policy_enforced=None, vault_id=None, kerberos_enabled=None, security_style=None, throughput_mibps=None, kerberos5_r=None, kerberos5_rw=None, kerberos5i_r=None, kerberos5i_rw=None, kerberos5p_r=None, kerberos5p_rw=None, has_root_access=None, snapshot_dir_visible=None, smb_encryption=None, smb_continuously_avl=None, encryption_key_source=None, rule_index=None, unix_read_only=None, unix_read_write=None, cifs=None, allowed_clients=None, ldap_enabled=None, chown_mode=None, cool_access=None, coolness_period=None, unix_permissions=None):
    params = get_params(locals())   
    command = "az netappfiles volume create " + params
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

def update(resource_group, account_name, pool_name, volume_name, usage_threshold=None, service_level=None, tags=None, vault_id=None, backup_enabled=None, backup_policy_id=None, policy_enforced=None, throughput_mibps=None, snapshot_policy_id=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az netappfiles volume update " + params
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

def revert(resource_group, account_name, pool_name, volume_name, snapshot_id):
    params = get_params(locals())   
    command = "az netappfiles volume revert " + params
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

def pool_change(resource_group, account_name, pool_name, volume_name, new_pool_resource_id):
    params = get_params(locals())   
    command = "az netappfiles volume pool-change " + params
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
