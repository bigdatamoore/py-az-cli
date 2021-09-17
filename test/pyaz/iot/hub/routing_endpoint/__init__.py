import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(hub_name, endpoint_name, endpoint_type, endpoint_resource_group, endpoint_subscription_id, connection_string=None, container_name=None, encoding=None, resource_group=None, batch_frequency=None, chunk_size=None, file_name_format=None, auth_type=None, endpoint_uri=None, entity_path=None, identity=None):
    params = get_params(locals())   
    command = "az iot hub routing-endpoint create " + params
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

def show(hub_name, endpoint_name, resource_group=None):
    params = get_params(locals())   
    command = "az iot hub routing-endpoint show " + params
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

def list(hub_name, endpoint_type=None, resource_group=None):
    params = get_params(locals())   
    command = "az iot hub routing-endpoint list " + params
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

def delete(hub_name, endpoint_name=None, endpoint_type=None, resource_group=None):
    params = get_params(locals())   
    command = "az iot hub routing-endpoint delete " + params
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
