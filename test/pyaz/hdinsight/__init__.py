import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def create(name, resource_group, type, location=None, tags=None, version=None, cluster_tier=None, cluster_configurations=None, component_version=None, headnode_size=None, workernode_size=None, zookeepernode_size=None, edgenode_size=None, kafka_management_node_size=None, kafka_management_node_count=None, kafka_client_group_id=None, kafka_client_group_name=None, workernode_count=None, workernode_data_disks_per_node=None, workernode_data_disk_storage_account_type=None, workernode_data_disk_size=None, http_user=None, http_password=None, ssh_user=None, ssh_password=None, ssh_public_key=None, storage_account=None, storage_account_key=None, storage_container=None, storage_filesystem=None, storage_account_managed_identity=None, vnet_name=None, subnet=None, domain=None, ldaps_urls=None, cluster_admin_account=None, cluster_admin_password=None, cluster_users_group_dns=None, assign_identity=None, minimal_tls_version=None, encryption_vault_uri=None, encryption_key_name=None, encryption_key_version=None, encryption_algorithm=None, encryption_in_transit=None, autoscale_type=None, autoscale_min_workernode_count=None, autoscale_max_workernode_count=None, timezone=None, days=None, time=None, autoscale_workernode_count=None, encryption_at_host=None, esp=None, idbroker=None, resource_provider_connection=None, enable_private_link=None, enable_compute_isolation=None, host_sku=None, no_validation_timeout=None, no_wait=None):
    params = get_params(locals())   
    command = "az hdinsight create " + params
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

def resize(name, resource_group, workernode_count, no_wait=None):
    params = get_params(locals())   
    command = "az hdinsight resize " + params
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

def show(resource_group, name):
    params = get_params(locals())   
    command = "az hdinsight show " + params
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
    command = "az hdinsight list " + params
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

def wait(resource_group, name, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az hdinsight wait " + params
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

def delete(resource_group, name, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az hdinsight delete " + params
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

def rotate_disk_encryption_key(resource_group, name, encryption_vault_uri, encryption_key_name, encryption_key_version, no_wait=None):
    params = get_params(locals())   
    command = "az hdinsight rotate-disk-encryption-key " + params
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

def update(name, resource_group, tags=None, no_wait=None):
    params = get_params(locals())   
    command = "az hdinsight update " + params
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

def list_usage(location):
    params = get_params(locals())   
    command = "az hdinsight list-usage " + params
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
