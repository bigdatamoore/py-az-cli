import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, gallery_name, gallery_image_definition, os_type, publisher, offer, sku, os_state=None, end_of_life_date=None, privacy_statement_uri=None, release_note_uri=None, eula=None, description=None, location=None, minimum_cpu_core=None, maximum_cpu_core=None, minimum_memory=None, maximum_memory=None, disallowed_disk_types=None, plan_name=None, plan_publisher=None, plan_product=None, tags=None, hyper_v_generation=None, features=None):
    params = get_params(locals())   
    command = "az sig image-definition create " + params
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

def list(resource_group, gallery_name):
    params = get_params(locals())   
    command = "az sig image-definition list " + params
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

def show(resource_group, gallery_name, gallery_image_definition):
    params = get_params(locals())   
    command = "az sig image-definition show " + params
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

def delete(resource_group, gallery_name, gallery_image_definition):
    params = get_params(locals())   
    command = "az sig image-definition delete " + params
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

def update(resource_group, gallery_name, gallery_image_definition, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az sig image-definition update " + params
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

def list_shared(location, gallery_unique_name, shared_to=None):
    params = get_params(locals())   
    command = "az sig image-definition list-shared " + params
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

def show_shared(location, gallery_unique_name, gallery_image_definition):
    params = get_params(locals())   
    command = "az sig image-definition show-shared " + params
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
