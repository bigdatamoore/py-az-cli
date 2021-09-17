import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def set(resource_group, name, docker_registry_server_url=None, docker_custom_image_name=None, docker_registry_server_user=None, enable_app_service_storage=None, docker_registry_server_password=None, multicontainer_config_type=None, multicontainer_config_file=None, slot=None):
    params = get_params(locals())   
    command = "az webapp config container set " + params
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

def delete(resource_group, name, slot=None):
    params = get_params(locals())   
    command = "az webapp config container delete " + params
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

def show(resource_group, name, show_multicontainer_config=None, slot=None):
    params = get_params(locals())   
    command = "az webapp config container show " + params
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
