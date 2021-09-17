import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, name):
    params = get_params(locals())   
    command = "az cdn endpoint rule action show " + params
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

def add(resource_group, profile_name, name, rule_name, action_name, cache_behavior=None, cache_duration=None, header_action=None, header_name=None, header_value=None, query_string_behavior=None, query_parameters=None, redirect_type=None, redirect_protocol=None, custom_hostname=None, custom_path=None, custom_querystring=None, custom_fragment=None, source_pattern=None, destination=None, preserve_unmatched_path=None, origin_group=None):
    params = get_params(locals())   
    command = "az cdn endpoint rule action add " + params
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

def remove(resource_group, profile_name, name, rule_name, index):
    params = get_params(locals())   
    command = "az cdn endpoint rule action remove " + params
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
