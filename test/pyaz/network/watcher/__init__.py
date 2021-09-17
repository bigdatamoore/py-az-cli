import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def configure(locations, resource_group=None, enabled=None, tags=None):
    params = get_params(locals())   
    command = "az network watcher configure " + params
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

def list():
    params = get_params(locals())   
    command = "az network watcher list " + params
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

def test_ip_flow(vm, __WATCHER_RG=None, __WATCHER_NAME=None, direction, protocol, local, remote, resource_group=None, nic=None, __LOCATION=None):
    params = get_params(locals())   
    command = "az network watcher test-ip-flow " + params
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

def test_connectivity(__WATCHER_RG=None, __WATCHER_NAME=None, source_resource, source_port=None, dest_resource=None, dest_port=None, dest_address=None, resource_group=None, protocol=None, method=None, headers=None, valid_status_codes=None):
    params = get_params(locals())   
    command = "az network watcher test-connectivity " + params
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

def show_next_hop(resource_group, vm, __WATCHER_RG=None, __WATCHER_NAME=None, source_ip, dest_ip, nic=None, __LOCATION=None):
    params = get_params(locals())   
    command = "az network watcher show-next-hop " + params
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

def show_security_group_view(resource_group, vm, __WATCHER_RG=None, __WATCHER_NAME=None, __LOCATION=None):
    params = get_params(locals())   
    command = "az network watcher show-security-group-view " + params
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

def show_topology(location=None, __RESOURCE_GROUP_NAME=None, __NETWORK_WATCHER_NAME=None, resource_group=None, vnet=None, subnet=None):
    params = get_params(locals())   
    command = "az network watcher show-topology " + params
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

def run_configuration_diagnostic(__WATCHER_RG=None, __WATCHER_NAME=None, resource, direction=None, protocol=None, source=None, destination=None, port=None, queries=None, resource_group=None, resource_type=None, parent=None):
    params = get_params(locals())   
    command = "az network watcher run-configuration-diagnostic " + params
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
