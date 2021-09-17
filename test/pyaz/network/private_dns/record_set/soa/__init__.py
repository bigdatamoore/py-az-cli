import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(resource_group, zone_name, record_type=None, name=None):
    params = get_params(locals())   
    command = "az network private-dns record-set soa show " + params
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

def update(resource_group, zone_name, host=None, email=None, serial_number=None, refresh_time=None, retry_time=None, expire_time=None, minimum_ttl=None):
    params = get_params(locals())   
    command = "az network private-dns record-set soa update " + params
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
