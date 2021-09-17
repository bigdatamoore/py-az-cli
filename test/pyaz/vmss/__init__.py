import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def create(name, resource_group, image=None, disable_overprovision=None, instance_count=None, location=None, tags=None, upgrade_policy_mode=None, validate=None, admin_username=None, admin_password=None, authentication_type=None, vm_sku=None, ssh_dest_key_path=None, ssh_key_values=None, generate_ssh_keys=None, load_balancer=None, lb_sku=None, app_gateway=None, app_gateway_subnet_address_prefix=None, app_gateway_sku=None, app_gateway_capacity=None, backend_pool_name=None, lb_nat_pool_name=None, backend_port=None, health_probe=None, public_ip_address=None, public_ip_address_allocation=None, public_ip_address_dns_name=None, accelerated_networking=None, public_ip_per_vm=None, vm_domain_name=None, dns_servers=None, nsg=None, os_disk_caching=None, data_disk_caching=None, storage_container_name=None, storage_sku=None, os_type=None, os_disk_name=None, use_unmanaged_disk=None, data_disk_sizes_gb=None, __DISK_INFO=None, vnet_name=None, vnet_address_prefix=None, subnet=None, subnet_address_prefix=None, __OS_OFFER=None, __OS_PUBLISHER=None, __OS_SKU=None, __OS_VERSION=None, __LOAD_BALANCER_TYPE=None, __APP_GATEWAY_TYPE=None, __VNET_TYPE=None, __PUBLIC_IP_ADDRESS_TYPE=None, __STORAGE_PROFILE=None, single_placement_group=None, custom_data=None, secrets=None, platform_fault_domain_count=None, plan_name=None, plan_product=None, plan_publisher=None, plan_promotion_code=None, license_type=None, assign_identity=None, scope=None, role=None, __IDENTITY_ROLE_ID=None, zones=None, priority=None, eviction_policy=None, asgs=None, ultra_ssd_enabled=None, ephemeral_os_disk=None, ppg=None, __AUX_SUBSCRIPTIONS=None, terminate_notification_time=None, max_price=None, computer_name_prefix=None, orchestration_mode=None, scale_in_policy=None, os_disk_encryption_set=None, data_disk_encryption_sets=None, data_disk_iops=None, data_disk_mbps=None, automatic_repairs_grace_period=None, specialized=None, os_disk_size_gb=None, encryption_at_host=None, host_group=None, max_batch_instance_percent=None, max_unhealthy_instance_percent=None, max_unhealthy_upgraded_instance_percent=None, pause_time_between_batches=None, enable_cross_zone_upgrade=None, prioritize_unhealthy_instances=None, edge_zone=None, user_data=None, network_api_version=None, enable_spot_restore=None, spot_restore_timeout=None, capacity_reservation_group=None, no_wait=None):
    params = get_params(locals())   
    command = "az vmss create " + params
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

def deallocate(resource_group, name, instance_ids=None, no_wait=None):
    params = get_params(locals())   
    command = "az vmss deallocate " + params
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

def delete(resource_group, name, force_deletion=None, no_wait=None):
    params = get_params(locals())   
    command = "az vmss delete " + params
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

def delete_instances(resource_group, name, instance_ids, no_wait=None):
    params = get_params(locals())   
    command = "az vmss delete-instances " + params
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

def get_instance_view(resource_group, name, instance_id=None):
    params = get_params(locals())   
    command = "az vmss get-instance-view " + params
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
    command = "az vmss list " + params
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

def list_instances(resource_group, name, filter=None, select=None, expand=None):
    params = get_params(locals())   
    command = "az vmss list-instances " + params
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

def list_instance_connection_info(resource_group, name):
    params = get_params(locals())   
    command = "az vmss list-instance-connection-info " + params
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

def list_instance_public_ips(resource_group, name):
    params = get_params(locals())   
    command = "az vmss list-instance-public-ips " + params
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

def list_skus(resource_group, name):
    params = get_params(locals())   
    command = "az vmss list-skus " + params
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

def reimage(resource_group, name, instance_id=None, no_wait=None):
    params = get_params(locals())   
    command = "az vmss reimage " + params
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

def perform_maintenance(resource_group, name, vm_instance_i_ds=None):
    params = get_params(locals())   
    command = "az vmss perform-maintenance " + params
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

def restart(resource_group, name, instance_ids=None, no_wait=None):
    params = get_params(locals())   
    command = "az vmss restart " + params
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

def scale(resource_group, name, new_capacity, no_wait=None):
    params = get_params(locals())   
    command = "az vmss scale " + params
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

def show(resource_group, name, instance_id=None, include_user_data=None):
    params = get_params(locals())   
    command = "az vmss show " + params
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

def simulate_eviction(resource_group, name, instance_id):
    params = get_params(locals())   
    command = "az vmss simulate-eviction " + params
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

def start(resource_group, name, instance_ids=None, no_wait=None):
    params = get_params(locals())   
    command = "az vmss start " + params
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

def stop(resource_group, name, instance_ids=None, skip_shutdown=None, no_wait=None):
    params = get_params(locals())   
    command = "az vmss stop " + params
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

def update(resource_group, name, instance_id=None, license_type=None, protect_from_scale_in=None, protect_from_scale_set_actions=None, enable_terminate_notification=None, terminate_notification_time=None, ultra_ssd_enabled=None, scale_in_policy=None, priority=None, max_price=None, ppg=None, enable_automatic_repairs=None, automatic_repairs_grace_period=None, max_batch_instance_percent=None, max_unhealthy_instance_percent=None, max_unhealthy_upgraded_instance_percent=None, pause_time_between_batches=None, enable_cross_zone_upgrade=None, prioritize_unhealthy_instances=None, user_data=None, enable_spot_restore=None, spot_restore_timeout=None, capacity_reservation_group=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az vmss update " + params
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

def update_instances(resource_group, name, instance_ids, no_wait=None):
    params = get_params(locals())   
    command = "az vmss update-instances " + params
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

def wait(resource_group, name, instance_id=None, __INCLUDE_USER_DATA=None, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az vmss wait " + params
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

def get_os_upgrade_history(resource_group, name):
    params = get_params(locals())   
    command = "az vmss get-os-upgrade-history " + params
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

def set_orchestration_service_state(resource_group, name, service_name, action, no_wait=None):
    params = get_params(locals())   
    command = "az vmss set-orchestration-service-state " + params
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
