import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, name, gallery_name=None, __LOCATION=None, output_name=None, is_vhd=None, artifact_tags=None, gallery_image_definition=None, gallery_replication_regions=None, managed_image=None, managed_image_location=None):
    params = get_params(locals())   
    command = "az image builder output add " + params
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

def remove(resource_group, name, output_name):
    params = get_params(locals())   
    command = "az image builder output remove " + params
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
    command = "az image builder output clear " + params
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
