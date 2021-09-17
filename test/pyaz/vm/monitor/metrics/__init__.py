import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def tail(resource_group, name, start_time=None, end_time=None, offset=None, interval=None, metadata=None, dimension=None, aggregation=None, metrics=None, filter=None, namespace=None, orderby=None, top=None):
    params = get_params(locals())   
    command = "az vm monitor metrics tail " + params
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

def list_definitions(resource_group, name, namespace=None):
    params = get_params(locals())   
    command = "az vm monitor metrics list-definitions " + params
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
