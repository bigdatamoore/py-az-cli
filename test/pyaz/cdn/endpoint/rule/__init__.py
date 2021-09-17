import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, name):
    params = get_params(locals())   
    command = "az cdn endpoint rule show " + params
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

def add(resource_group, profile_name, name, order, action_name, match_variable=None, operator=None, match_values=None, selector=None, negate_condition=None, transform=None, cache_behavior=None, cache_duration=None, header_action=None, header_name=None, header_value=None, query_string_behavior=None, query_parameters=None, redirect_type=None, redirect_protocol=None, custom_hostname=None, custom_path=None, custom_querystring=None, custom_fragment=None, source_pattern=None, destination=None, preserve_unmatched_path=None, rule_name=None, origin_group=None):
    params = get_params(locals())   
    command = "az cdn endpoint rule add " + params
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

def remove(resource_group, profile_name, name, rule_name=None, order=None):
    params = get_params(locals())   
    command = "az cdn endpoint rule remove " + params
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
