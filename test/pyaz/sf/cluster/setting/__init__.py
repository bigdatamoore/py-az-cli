import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def set(resource_group, cluster_name, section=None, parameter=None, value=None, settings_section_description=None):
    params = get_params(locals())   
    command = "az sf cluster setting set " + params
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

def remove(resource_group, cluster_name, section=None, parameter=None, settings_section_description=None):
    params = get_params(locals())   
    command = "az sf cluster setting remove " + params
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
