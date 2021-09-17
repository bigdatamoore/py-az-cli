import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, lab_name, name, expand=None):
    params = get_params(locals())   
    command = "az lab vm show " + params
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

def delete(resource_group, lab_name, name):
    params = get_params(locals())   
    command = "az lab vm delete " + params
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

def start(resource_group, lab_name, name):
    params = get_params(locals())   
    command = "az lab vm start " + params
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

def stop(resource_group, lab_name, name):
    params = get_params(locals())   
    command = "az lab vm stop " + params
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

def apply_artifacts(resource_group, lab_name, name, artifacts=None):
    params = get_params(locals())   
    command = "az lab vm apply-artifacts " + params
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

def list(resource_group, lab_name, order_by=None, top=None, filters=None, all=None, claimable=None, environment=None, expand=None, object_id=None):
    params = get_params(locals())   
    command = "az lab vm list " + params
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

def claim(lab_name=None, name=None, resource_group=None):
    params = get_params(locals())   
    command = "az lab vm claim " + params
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

def create(resource_group, lab_name, name, notes=None, image=None, image_type=None, size=None, admin_username=None, admin_password=None, ssh_key=None, authentication_type=None, vnet_name=None, subnet=None, __DISALLOW_PUBLIC_IP_ADDRESS=None, artifacts=None, __LOCATION=None, tags=None, __CUSTOM_IMAGE_ID=None, __LAB_VIRTUAL_NETWORK_ID=None, __GALLERY_IMAGE_REFERENCE=None, generate_ssh_keys=None, allow_claim=None, disk_type=None, expiration_date=None, formula=None, ip_configuration=None, __NETWORK_INTERFACE=None, __OS_TYPE=None, saved_secret=None):
    params = get_params(locals())   
    command = "az lab vm create " + params
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
