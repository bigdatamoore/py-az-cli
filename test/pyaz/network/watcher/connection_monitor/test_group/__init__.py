import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def add(connection_monitor, __WATCHER_RG=None, __WATCHER_NAME=None, location, name, endpoint_source_name, endpoint_dest_name, test_config_name, disable=None, endpoint_source_resource_id=None, endpoint_source_address=None, endpoint_dest_resource_id=None, endpoint_dest_address=None, frequency=None, protocol=None, preferred_ip_version=None, threshold_failed_percent=None, threshold_round_trip_time=None, tcp_disable_trace_route=None, tcp_port=None, icmp_disable_trace_route=None, http_port=None, http_method=None, http_path=None, http_valid_status_codes=None, https_prefer=None):
    params = get_params(locals())   
    command = "az network watcher connection-monitor test-group add " + params
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

def remove(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location, name):
    params = get_params(locals())   
    command = "az network watcher connection-monitor test-group remove " + params
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

def show(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location, name):
    params = get_params(locals())   
    command = "az network watcher connection-monitor test-group show " + params
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

def list(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location):
    params = get_params(locals())   
    command = "az network watcher connection-monitor test-group list " + params
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
