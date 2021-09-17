import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, autoscale_name, condition, scale, profile_name=None, cooldown=None, resource=None, timegrain=None):
    params = get_params(locals())   
    command = "az monitor autoscale rule create " + params
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

def list(autoscale_name, resource_group, profile_name=None):
    params = get_params(locals())   
    command = "az monitor autoscale rule list " + params
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

def delete(autoscale_name, resource_group, index, profile_name=None):
    params = get_params(locals())   
    command = "az monitor autoscale rule delete " + params
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

def copy(autoscale_name, resource_group, dest_schedule, index, source_schedule=None):
    params = get_params(locals())   
    command = "az monitor autoscale rule copy " + params
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
