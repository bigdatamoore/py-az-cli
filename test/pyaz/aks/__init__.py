import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def browse(resource_group, name, disable_browser=None, listen_address=None, listen_port=None):
    params = get_params(locals())   
    command = "az aks browse " + params
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

def create(resource_group, name, ssh_key_value=None, dns_name_prefix=None, location=None, admin_username=None, windows_admin_username=None, windows_admin_password=None, enable_ahub=None, kubernetes_version=None, node_vm_size=None, node_osdisk_type=None, node_osdisk_size=None, node_osdisk_diskencryptionset_id=None, node_count=None, nodepool_name=None, nodepool_tags=None, nodepool_labels=None, service_principal=None, client_secret=None, no_ssh_key=None, disable_rbac=None, enable_rbac=None, vm_set_type=None, skip_subnet_role_assignment=None, os_sku=None, enable_cluster_autoscaler=None, cluster_autoscaler_profile=None, network_plugin=None, network_policy=None, uptime_sla=None, pod_cidr=None, service_cidr=None, dns_service_ip=None, docker_bridge_address=None, load_balancer_sku=None, load_balancer_managed_outbound_ip_count=None, load_balancer_outbound_ips=None, load_balancer_outbound_ip_prefixes=None, load_balancer_outbound_ports=None, load_balancer_idle_timeout=None, outbound_type=None, auto_upgrade_channel=None, enable_addons=None, workspace_resource_id=None, vnet_subnet_id=None, ppg=None, max_pods=None, min_count=None, max_count=None, aad_client_app_id=None, aad_server_app_id=None, aad_server_app_secret=None, aad_tenant_id=None, tags=None, zones=None, enable_node_public_ip=None, node_public_ip_prefix_id=None, generate_ssh_keys=None, api_server_authorized_ip_ranges=None, enable_private_cluster=None, private_dns_zone=None, fqdn_subdomain=None, disable_public_fqdn=None, enable_managed_identity=None, assign_identity=None, attach_acr=None, enable_aad=None, aad_admin_group_object_ids=None, aci_subnet_name=None, appgw_name=None, appgw_subnet_cidr=None, appgw_id=None, appgw_subnet_id=None, appgw_watch_namespace=None, enable_sgxquotehelper=None, enable_encryption_at_host=None, assign_kubelet_identity=None, enable_ultra_ssd=None, edge_zone=None, yes=None, enable_azure_rbac=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks create " + params
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

def update(resource_group, name, enable_cluster_autoscaler=None, disable_cluster_autoscaler=None, update_cluster_autoscaler=None, cluster_autoscaler_profile=None, min_count=None, max_count=None, uptime_sla=None, no_uptime_sla=None, load_balancer_managed_outbound_ip_count=None, load_balancer_outbound_ips=None, load_balancer_outbound_ip_prefixes=None, load_balancer_outbound_ports=None, load_balancer_idle_timeout=None, attach_acr=None, detach_acr=None, api_server_authorized_ip_ranges=None, enable_aad=None, aad_tenant_id=None, aad_admin_group_object_ids=None, enable_ahub=None, disable_ahub=None, windows_admin_password=None, auto_upgrade_channel=None, enable_managed_identity=None, assign_identity=None, yes=None, enable_public_fqdn=None, disable_public_fqdn=None, enable_azure_rbac=None, disable_azure_rbac=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks update " + params
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
    command = "az aks delete " + params
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

def update_credentials(resource_group, name, reset_service_principal=None, reset_aad=None, service_principal=None, client_secret=None, aad_server_app_id=None, aad_server_app_secret=None, aad_client_app_id=None, aad_tenant_id=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks update-credentials " + params
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

def disable_addons(resource_group, name, addons, no_wait=None):
    params = get_params(locals())   
    command = "az aks disable-addons " + params
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

def enable_addons(resource_group, name, addons, workspace_resource_id=None, subnet_name=None, appgw_name=None, appgw_subnet_cidr=None, appgw_id=None, appgw_subnet_id=None, appgw_watch_namespace=None, enable_sgxquotehelper=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks enable-addons " + params
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

def get_credentials(resource_group, name, admin=None, file=None, overwrite_existing=None, context=None, public_fqdn=None):
    params = get_params(locals())   
    command = "az aks get-credentials " + params
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

def check_acr(resource_group, name, acr):
    params = get_params(locals())   
    command = "az aks check-acr " + params
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

def get_upgrades(resource_group, name):
    params = get_params(locals())   
    command = "az aks get-upgrades " + params
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

def install_cli(client_version=None, install_location=None, base_src_url=None, kubelogin_version=None, kubelogin_install_location=None, kubelogin_base_src_url=None):
    params = get_params(locals())   
    command = "az aks install-cli " + params
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
    command = "az aks list " + params
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

def remove_dev_spaces(name, resource_group, yes=None):
    params = get_params(locals())   
    command = "az aks remove-dev-spaces " + params
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

def scale(resource_group, name, node_count, nodepool_name=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks scale " + params
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
    command = "az aks show " + params
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

def upgrade(resource_group, name, kubernetes_version=None, control_plane_only=None, node_image_only=None, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks upgrade " + params
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

def use_dev_spaces(name, resource_group, update=None, space=None, endpoint=None, yes=None):
    params = get_params(locals())   
    command = "az aks use-dev-spaces " + params
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

def rotate_certs(resource_group, name, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks rotate-certs " + params
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
    command = "az aks wait " + params
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

def stop(resource_group, name, no_wait=None):
    params = get_params(locals())   
    command = "az aks stop " + params
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
    command = "az aks start " + params
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

def get_versions(location):
    params = get_params(locals())   
    command = "az aks get-versions " + params
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
