import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group, cluster_name):
    params = get_params(locals())   
    command = "az sf managed-node-type list " + params
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

def delete(resource_group, cluster_name, _n):
    params = get_params(locals())   
    command = "az sf managed-node-type delete " + params
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

def show(resource_group, cluster_name, _n):
    params = get_params(locals())   
    command = "az sf managed-node-type show " + params
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

def create(resource_group, cluster_name, _n, instance_count, primary=None, disk_size=None, disk_type=None, application_start_port=None, application_end_port=None, ephemeral_start_port=None, ephemeral_end_port=None, vm_size=None, vm_image_publisher=None, vm_image_offer=None, vm_image_sku=None, vm_image_version=None, capacity=None, placement_property=None, is_stateless=None, multiple_placement_groups=None):
    params = get_params(locals())   
    command = "az sf managed-node-type create " + params
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

def update(resource_group, cluster_name, _n, instance_count=None, application_start_port=None, application_end_port=None, ephemeral_start_port=None, ephemeral_end_port=None, capacity=None, placement_property=None):
    params = get_params(locals())   
    command = "az sf managed-node-type update " + params
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
