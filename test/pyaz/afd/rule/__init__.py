import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, rule_set_name, rule_name):
    params = get_params(locals())   
    command = "az afd rule show " + params
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

def list(resource_group, profile_name, rule_set_name):
    params = get_params(locals())   
    command = "az afd rule list " + params
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

def create(resource_group, profile_name, rule_set_name, order, rule_name, action_name, match_variable=None, operator=None, match_values=None, selector=None, negate_condition=None, transform=None, cache_behavior=None, cache_duration=None, header_action=None, header_name=None, header_value=None, query_string_behavior=None, query_parameters=None, redirect_type=None, redirect_protocol=None, custom_hostname=None, custom_path=None, custom_querystring=None, custom_fragment=None, source_pattern=None, destination=None, preserve_unmatched_path=None, match_processing_behavior=None):
    params = get_params(locals())   
    command = "az afd rule create " + params
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

def delete(resource_group, profile_name, rule_set_name, rule_name, yes=None):
    params = get_params(locals())   
    command = "az afd rule delete " + params
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
