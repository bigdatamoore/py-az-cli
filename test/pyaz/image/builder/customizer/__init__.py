import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, name, customizer_name, type, script_url=None, inline_script=None, exit_codes=None, restart_command=None, restart_check_command=None, restart_timeout=None, file_source=None, dest_path=None, search_criteria=None, filters=None, update_limit=None):
    params = get_params(locals())   
    command = "az image builder customizer add " + params
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

def remove(resource_group, name, customizer_name):
    params = get_params(locals())   
    command = "az image builder customizer remove " + params
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

def clear(resource_group, name):
    params = get_params(locals())   
    command = "az image builder customizer clear " + params
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
