import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group, lab_name, artifact_source_name, expand=None, filter=None, top=None, orderby=None):
    params = get_params(locals())   
    command = "az lab arm-template list " + params
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

def show(resource_group, lab_name, name, artifact_source_name, export_parameters=None):
    params = get_params(locals())   
    command = "az lab arm-template show " + params
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
