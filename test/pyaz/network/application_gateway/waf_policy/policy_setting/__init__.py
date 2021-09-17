import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def list(resource_group, policy_name):
    params = get_params(locals())   
    command = "az network application-gateway waf-policy policy-setting list " + params
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

def update(resource_group, policy_name, state=None, mode=None, max_request_body_size_in_kb=None, file_upload_limit_in_mb=None, request_body_check=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network application-gateway waf-policy policy-setting update " + params
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
