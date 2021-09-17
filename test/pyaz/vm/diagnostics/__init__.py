import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def set(resource_group, vm_name, settings, protected_settings=None, version=None, no_auto_upgrade_minor_version=None):
    params = get_params(locals())   
    command = "az vm diagnostics set " + params
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

def get_default_config(is_windows_os=None):
    params = get_params(locals())   
    command = "az vm diagnostics get-default-config " + params
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
