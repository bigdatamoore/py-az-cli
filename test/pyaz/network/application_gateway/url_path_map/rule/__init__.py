import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def create(resource_group, gateway_name, path_map_name, name, paths, address_pool=None, http_settings=None, redirect_config=None, waf_policy=None, rewrite_rule_set=None, no_wait=None):
    params = get_params(locals())   
    command = "az network application-gateway url-path-map rule create " + params
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

def delete(resource_group, gateway_name, path_map_name, name, no_wait=None):
    params = get_params(locals())   
    command = "az network application-gateway url-path-map rule delete " + params
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
