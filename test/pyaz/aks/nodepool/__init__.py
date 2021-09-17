import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group, cluster_name):
    params = get_params(locals())   
    command = "az aks nodepool list " + params
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

def show(resource_group, cluster_name, name):
    params = get_params(locals())   
    command = "az aks nodepool show " + params
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

def add(resource_group, cluster_name, name, kubernetes_version=None, zones=None, enable_node_public_ip=None, node_public_ip_prefix_id=None, node_vm_size=None, node_osdisk_type=None, node_osdisk_size=None, node_count=None, vnet_subnet_id=None, ppg=None, max_pods=None, os_type=None, os_sku=None, min_count=None, max_count=None, enable_cluster_autoscaler=None, node_taints=None, priority=None, eviction_policy=None, spot_max_price=None, tags=None, labels=None, max_surge=None, mode=None, enable_encryption_at_host=None, enable_ultra_ssd=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks nodepool add " + params
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

def scale(resource_group, cluster_name, name, node_count=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks nodepool scale " + params
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

def upgrade(resource_group, cluster_name, name, kubernetes_version=None, node_image_only=None, max_surge=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks nodepool upgrade " + params
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

def update(resource_group, cluster_name, name, enable_cluster_autoscaler=None, disable_cluster_autoscaler=None, update_cluster_autoscaler=None, min_count=None, max_count=None, tags=None, max_surge=None, mode=None, no_wait=None):
    params = get_params(locals())   
    command = "az aks nodepool update " + params
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

def delete(resource_group, cluster_name, name, no_wait=None):
    params = get_params(locals())   
    command = "az aks nodepool delete " + params
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

def get_upgrades(resource_group, cluster_name, nodepool_name):
    params = get_params(locals())   
    command = "az aks nodepool get-upgrades " + params
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
