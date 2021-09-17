import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def capture(resource_group, name, vhd_name_prefix, storage_container=None, overwrite=None):
    params = get_params(locals())   
    command = "az vm capture " + params
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

def create(name, resource_group, image=None, size=None, location=None, tags=None, authentication_type=None, admin_password=None, computer_name=None, admin_username=None, ssh_dest_key_path=None, ssh_key_values=None, generate_ssh_keys=None, availability_set=None, nics=None, nsg=None, nsg_rule=None, accelerated_networking=None, private_ip_address=None, public_ip_address=None, public_ip_address_allocation=None, public_ip_address_dns_name=None, public_ip_sku=None, os_disk_name=None, os_type=None, storage_account=None, os_disk_caching=None, data_disk_caching=None, storage_container_name=None, storage_sku=None, use_unmanaged_disk=None, attach_os_disk=None, os_disk_size_gb=None, attach_data_disks=None, data_disk_sizes_gb=None, __DISK_INFO=None, vnet_name=None, vnet_address_prefix=None, subnet=None, subnet_address_prefix=None, __STORAGE_PROFILE=None, __OS_PUBLISHER=None, __OS_OFFER=None, __OS_SKU=None, __OS_VERSION=None, __STORAGE_ACCOUNT_TYPE=None, __VNET_TYPE=None, __NSG_TYPE=None, __PUBLIC_IP_ADDRESS_TYPE=None, __NIC_TYPE=None, validate=None, custom_data=None, secrets=None, plan_name=None, plan_product=None, plan_publisher=None, plan_promotion_code=None, license_type=None, assign_identity=None, scope=None, role=None, __IDENTITY_ROLE_ID=None, asgs=None, zone=None, boot_diagnostics_storage=None, ultra_ssd_enabled=None, ephemeral_os_disk=None, ppg=None, host=None, host_group=None, __AUX_SUBSCRIPTIONS=None, priority=None, max_price=None, eviction_policy=None, enable_agent=None, workspace=None, vmss=None, os_disk_encryption_set=None, data_disk_encryption_sets=None, specialized=None, encryption_at_host=None, enable_auto_update=None, patch_mode=None, ssh_key_name=None, enable_hotpatching=None, platform_fault_domain=None, security_type=None, enable_secure_boot=None, enable_vtpm=None, count=None, edge_zone=None, nic_delete_option=None, os_disk_delete_option=None, data_disk_delete_option=None, user_data=None, capacity_reservation_group=None, no_wait=None):
    params = get_params(locals())   
    command = "az vm create " + params
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

def convert(resource_group, name):
    params = get_params(locals())   
    command = "az vm convert " + params
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

def deallocate(resource_group, name, no_wait=None):
    params = get_params(locals())   
    command = "az vm deallocate " + params
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

def delete(resource_group, name, force_deletion=None, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az vm delete " + params
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

def generalize(resource_group, name, no_wait=None):
    params = get_params(locals())   
    command = "az vm generalize " + params
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

def get_instance_view(resource_group, name, __INCLUDE_USER_DATA=None):
    params = get_params(locals())   
    command = "az vm get-instance-view " + params
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

def list(resource_group=None, show_details=None):
    params = get_params(locals())   
    command = "az vm list " + params
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

def list_ip_addresses(resource_group=None, name=None):
    params = get_params(locals())   
    command = "az vm list-ip-addresses " + params
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

def list_sizes(location):
    params = get_params(locals())   
    command = "az vm list-sizes " + params
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

def list_skus(location=None, size=None, zone=None, all=None, resource_type=None):
    params = get_params(locals())   
    command = "az vm list-skus " + params
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
    command = "az vm list-usage " + params
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

def list_vm_resize_options(resource_group, name):
    params = get_params(locals())   
    command = "az vm list-vm-resize-options " + params
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

def open_port(resource_group, name, port, priority=None, nsg_name=None, apply_to_subnet=None):
    params = get_params(locals())   
    command = "az vm open-port " + params
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

def perform_maintenance(resource_group, name):
    params = get_params(locals())   
    command = "az vm perform-maintenance " + params
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

def redeploy(resource_group, name, no_wait=None):
    params = get_params(locals())   
    command = "az vm redeploy " + params
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

def resize(resource_group, name, size, no_wait=None):
    params = get_params(locals())   
    command = "az vm resize " + params
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

def restart(resource_group, name, force=None, no_wait=None):
    params = get_params(locals())   
    command = "az vm restart " + params
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

def show(resource_group, name, show_details=None, include_user_data=None):
    params = get_params(locals())   
    command = "az vm show " + params
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

def simulate_eviction(resource_group, name):
    params = get_params(locals())   
    command = "az vm simulate-eviction " + params
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

def start(resource_group, name, no_wait=None):
    params = get_params(locals())   
    command = "az vm start " + params
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

def stop(resource_group, name, skip_shutdown=None, no_wait=None):
    params = get_params(locals())   
    command = "az vm stop " + params
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

def reapply(resource_group, name, no_wait=None):
    params = get_params(locals())   
    command = "az vm reapply " + params
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

def update(resource_group, name, os_disk=None, disk_caching=None, write_accelerator=None, license_type=None, ultra_ssd_enabled=None, priority=None, max_price=None, ppg=None, workspace=None, enable_secure_boot=None, enable_vtpm=None, user_data=None, capacity_reservation_group=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az vm update " + params
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

def wait(resource_group, name, __INCLUDE_USER_DATA=None, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az vm wait " + params
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

def auto_shutdown(resource_group, name, off=None, email=None, webhook=None, time=None, location=None):
    params = get_params(locals())   
    command = "az vm auto-shutdown " + params
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

def assess_patches(resource_group, name):
    params = get_params(locals())   
    command = "az vm assess-patches " + params
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

def install_patches(resource_group, name, maximum_duration, reboot_setting, classifications_to_include_win=None, classifications_to_include_linux=None, kb_numbers_to_include=None, kb_numbers_to_exclude=None, exclude_kbs_requiring_reboot=None, package_name_masks_to_include=None, package_name_masks_to_exclude=None, no_wait=None):
    params = get_params(locals())   
    command = "az vm install-patches " + params
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
