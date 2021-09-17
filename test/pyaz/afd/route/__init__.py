import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, profile_name, endpoint_name, route_name):
    params = get_params(locals())   
    command = "az afd route show " + params
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

def list(resource_group, profile_name, endpoint_name):
    params = get_params(locals())   
    command = "az afd route list " + params
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

def create(resource_group, profile_name, endpoint_name, route_name, https_redirect, supported_protocols, origin_group, forwarding_protocol, link_to_default_domain=None, enable_compression=None, content_types_to_compress=None, query_string_caching_behavior=None, custom_domains=None, origin_path=None, patterns_to_match=None, rule_sets=None):
    params = get_params(locals())   
    command = "az afd route create " + params
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

def update(resource_group, profile_name, endpoint_name, route_name, https_redirect=None, supported_protocols=None, origin_group=None, forwarding_protocol=None, link_to_default_domain=None, enable_compression=None, content_types_to_compress=None, query_string_caching_behavior=None, custom_domains=None, origin_path=None, patterns_to_match=None, rule_sets=None):
    params = get_params(locals())   
    command = "az afd route update " + params
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

def delete(resource_group, profile_name, endpoint_name, route_name, yes=None):
    params = get_params(locals())   
    command = "az afd route delete " + params
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
