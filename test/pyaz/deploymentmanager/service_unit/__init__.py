import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, service_topology_name, service_name, service_unit_name, target_resource_group, deployment_mode, parameters_path, template_path, location=None, tags=None):
    params = get_params(locals())   
    command = "az deploymentmanager service-unit create " + params
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

def delete(resource_group, service_topology_name, service_name, service_unit_name):
    params = get_params(locals())   
    command = "az deploymentmanager service-unit delete " + params
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

def show(resource_group, service_topology_name, service_name, service_unit_name):
    params = get_params(locals())   
    command = "az deploymentmanager service-unit show " + params
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

def list(resource_group, service_topology_name, service_name):
    params = get_params(locals())   
    command = "az deploymentmanager service-unit list " + params
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

def update(resource_group, service_topology_name, service_name, service_unit_name, target_resource_group=None, deployment_mode=None, parameters_path=None, template_path=None, tags=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az deploymentmanager service-unit update " + params
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
