import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, service_name, __SEARCH_MANAGEMENT_REQUEST_OPTIONS=None):
    params = get_params(locals())   
    command = "az search admin-key show " + params
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

def renew(resource_group, service_name, key_kind, __SEARCH_MANAGEMENT_REQUEST_OPTIONS=None):
    params = get_params(locals())   
    command = "az search admin-key renew " + params
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
