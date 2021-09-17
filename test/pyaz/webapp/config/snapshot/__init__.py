import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, name, slot=None):
    params = get_params(locals())   
    command = "az webapp config snapshot list " + params
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

def restore(resource_group, name, time, slot=None, restore_content_only=None, source_resource_group=None, source_name=None, source_slot=None):
    params = get_params(locals())   
    command = "az webapp config snapshot restore " + params
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
