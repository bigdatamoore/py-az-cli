import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, origin_group_name):
    params = get_params(locals())   
    command = "az afd origin-group show " + params
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

def list(resource_group, profile_name):
    params = get_params(locals())   
    command = "az afd origin-group list " + params
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

def create(resource_group, profile_name, origin_group_name, sample_size, successful_samples_required, additional_latency_in_milliseconds, probe_request_type, probe_protocol, probe_path, probe_interval_in_seconds=None):
    params = get_params(locals())   
    command = "az afd origin-group create " + params
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

def update(resource_group, profile_name, origin_group_name, sample_size=None, successful_samples_required=None, additional_latency_in_milliseconds=None, probe_request_type=None, probe_protocol=None, probe_path=None, probe_interval_in_seconds=None):
    params = get_params(locals())   
    command = "az afd origin-group update " + params
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

def delete(resource_group, profile_name, origin_group_name, yes=None):
    params = get_params(locals())   
    command = "az afd origin-group delete " + params
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
