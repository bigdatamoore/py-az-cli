import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(name, __WATCHER_RG=None, __WATCHER_NAME=None, resource_group=None, location=None, source_resource=None, source_port=None, dest_resource=None, dest_port=None, dest_address=None, tags=None, do_not_start=None, monitoring_interval=None, endpoint_source_name=None, endpoint_source_resource_id=None, endpoint_source_address=None, endpoint_source_type=None, endpoint_source_coverage_level=None, endpoint_dest_name=None, endpoint_dest_resource_id=None, endpoint_dest_address=None, endpoint_dest_type=None, endpoint_dest_coverage_level=None, test_config_name=None, frequency=None, protocol=None, preferred_ip_version=None, threshold_failed_percent=None, threshold_round_trip_time=None, tcp_disable_trace_route=None, tcp_port=None, tcp_port_behavior=None, icmp_disable_trace_route=None, http_port=None, http_method=None, http_path=None, http_valid_status_codes=None, https_prefer=None, test_group_name=None, test_group_disable=None, output_type=None, workspace_ids=None, notes=None):
    params = get_params(locals())   
    command = "az network watcher connection-monitor create " + params
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

def delete(location, resource_group=None, __NETWORK_WATCHER_NAME=None, name):
    params = get_params(locals())   
    command = "az network watcher connection-monitor delete " + params
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

def show(location, resource_group=None, __NETWORK_WATCHER_NAME=None, name):
    params = get_params(locals())   
    command = "az network watcher connection-monitor show " + params
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

def stop(location, resource_group=None, __NETWORK_WATCHER_NAME=None, name):
    params = get_params(locals())   
    command = "az network watcher connection-monitor stop " + params
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

def start(location, resource_group=None, __NETWORK_WATCHER_NAME=None, name):
    params = get_params(locals())   
    command = "az network watcher connection-monitor start " + params
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

def query(location, resource_group=None, __NETWORK_WATCHER_NAME=None, name):
    params = get_params(locals())   
    command = "az network watcher connection-monitor query " + params
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

def list(location, resource_group=None, __NETWORK_WATCHER_NAME=None):
    params = get_params(locals())   
    command = "az network watcher connection-monitor list " + params
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
