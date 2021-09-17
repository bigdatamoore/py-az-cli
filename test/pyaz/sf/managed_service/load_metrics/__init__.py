import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(resource_group, cluster_name, application, name, metric_name, weight=None, primary_default_load=None, secondary_default_load=None, default_load=None):
    params = get_params(locals())   
    command = "az sf managed-service load-metrics create " + params
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

def update(resource_group, cluster_name, application, name, metric_name, weight=None, primary_default_load=None, secondary_default_load=None, default_load=None):
    params = get_params(locals())   
    command = "az sf managed-service load-metrics update " + params
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

def delete(resource_group, cluster_name, application, name, metric_name):
    params = get_params(locals())   
    command = "az sf managed-service load-metrics delete " + params
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
