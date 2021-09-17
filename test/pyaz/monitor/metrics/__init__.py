import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, resource, start_time=None, end_time=None, offset=None, interval=None, metadata=None, dimension=None, aggregation=None, metrics=None, filter=None, namespace=None, orderby=None, top=None):
    params = get_params(locals())   
    command = "az monitor metrics list " + params
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

def list_definitions(resource_namespace=None, resource_parent=None, resource_type=None, resource_group=None, resource, namespace=None):
    params = get_params(locals())   
    command = "az monitor metrics list-definitions " + params
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

def list_namespaces(resource_uri, start_time=None):
    params = get_params(locals())   
    command = "az monitor metrics list-namespaces " + params
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
