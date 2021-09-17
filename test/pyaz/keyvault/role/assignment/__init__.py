import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def delete(name=None, scope=None, assignee=None, role=None, assignee_object_id=None, ids=None, hsm_name=None, id=None):
    params = get_params(locals())   
    command = "az keyvault role assignment delete " + params
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

def list(scope=None, assignee=None, role=None, assignee_object_id=None, hsm_name=None, id=None):
    params = get_params(locals())   
    command = "az keyvault role assignment list " + params
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

def create(role, scope, assignee_object_id=None, name=None, assignee=None, assignee_principal_type=None, hsm_name=None, id=None):
    params = get_params(locals())   
    command = "az keyvault role assignment create " + params
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
