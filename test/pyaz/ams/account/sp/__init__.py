import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(account_name, resource_group, name=None, new_sp_name=None, role=None, password=None, xml=None, years=None):
    params = get_params(locals())   
    command = "az ams account sp create " + params
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

def reset_credentials(account_name, resource_group, name=None, role=None, password=None, xml=None, years=None):
    params = get_params(locals())   
    command = "az ams account sp reset-credentials " + params
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
