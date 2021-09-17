import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def attach(resource_group, vmss_name, size_gb=None, instance_id=None, lun=None, caching=None, disk=None, sku=None):
    params = get_params(locals())   
    command = "az vmss disk attach " + params
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

def detach(resource_group, vmss_name, lun, instance_id=None):
    params = get_params(locals())   
    command = "az vmss disk detach " + params
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
