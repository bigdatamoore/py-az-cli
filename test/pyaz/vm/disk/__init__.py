import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def attach(resource_group, vm_name, name, new=None, sku=None, size_gb=None, lun=None, caching=None, enable_write_accelerator=None):
    params = get_params(locals())   
    command = "az vm disk attach " + params
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

def detach(resource_group, vm_name, name):
    params = get_params(locals())   
    command = "az vm disk detach " + params
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
