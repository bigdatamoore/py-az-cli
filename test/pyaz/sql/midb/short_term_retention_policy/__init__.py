import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def set(deleted_time=None, retention_days, name, managed_instance, resource_group, no_wait=None):
    params = get_params(locals())   
    command = "az sql midb short-term-retention-policy set " + params
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

def show(name, managed_instance, resource_group, deleted_time=None):
    params = get_params(locals())   
    command = "az sql midb short-term-retention-policy show " + params
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
