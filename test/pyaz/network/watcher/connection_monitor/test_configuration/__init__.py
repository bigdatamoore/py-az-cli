import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def add(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location, name, protocol, test_groups, frequency=None, threshold_failed_percent=None, threshold_round_trip_time=None, preferred_ip_version=None, tcp_port=None, tcp_port_behavior=None, tcp_disable_trace_route=None, icmp_disable_trace_route=None, http_port=None, http_method=None, http_path=None, http_valid_status_codes=None, http_prefer_https=None, http_request_header=None):
    params = get_params(locals())   
    command = "az network watcher connection-monitor test-configuration add " + params
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

def remove(__WATCHER_RG=None, __WATCHER_NAME=None, connection_monitor, location, name, test_groups=None):
    params = get_params(locals())   
    command = "az network watcher connection-monitor test-configuration remove " + params
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
    command = "az network watcher connection-monitor test-configuration show " + params
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
    command = "az network watcher connection-monitor test-configuration list " + params
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
