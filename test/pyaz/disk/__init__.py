import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def create(resource_group, name, location=None, size_gb=None, sku=None, os_type=None, source=None, for_upload=None, upload_size_bytes=None, __SOURCE_BLOB_URI=None, __SOURCE_DISK=None, __SOURCE_SNAPSHOT=None, source_storage_account_id=None, tags=None, zone=None, disk_iops_read_write=None, disk_mbps_read_write=None, hyper_v_generation=None, encryption_type=None, disk_encryption_set=None, max_shares=None, disk_iops_read_only=None, disk_mbps_read_only=None, image_reference=None, image_reference_lun=None, gallery_image_reference=None, gallery_image_reference_lun=None, network_access_policy=None, disk_access=None, logical_sector_size=None, tier=None, enable_bursting=None, edge_zone=None, security_type=None, support_hibernation=None, no_wait=None):
    params = get_params(locals())   
    command = "az disk create " + params
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
    command = "az disk delete " + params
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

def grant_access(resource_group, name, duration_in_seconds, access_level=None):
    params = get_params(locals())   
    command = "az disk grant-access " + params
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
    command = "az disk list " + params
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

def revoke_access(resource_group, name):
    params = get_params(locals())   
    command = "az disk revoke-access " + params
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
    command = "az disk show " + params
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

def update(resource_group, name, size_gb=None, sku=None, disk_iops_read_write=None, disk_mbps_read_write=None, encryption_type=None, disk_encryption_set=None, network_access_policy=None, disk_access=None, max_shares=None, disk_iops_read_only=None, disk_mbps_read_only=None, enable_bursting=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az disk update " + params
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
    command = "az disk wait " + params
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
