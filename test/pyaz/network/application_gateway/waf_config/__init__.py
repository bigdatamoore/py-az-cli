import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def set(resource_group, gateway_name, enabled, firewall_mode=None, rule_set_type=None, rule_set_version=None, disabled_rule_groups=None, disabled_rules=None, request_body_check=None, max_request_body_size=None, file_upload_limit=None, exclusion=None, no_wait=None):
    params = get_params(locals())   
    command = "az network application-gateway waf-config set " + params
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

def show(resource_group, gateway_name):
    params = get_params(locals())   
    command = "az network application-gateway waf-config show " + params
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

def list_rule_sets(type=None, version=None, group=None):
    params = get_params(locals())   
    command = "az network application-gateway waf-config list-rule-sets " + params
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
