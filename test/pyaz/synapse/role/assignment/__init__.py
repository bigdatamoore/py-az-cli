import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(workspace_name, role, assignee=None, assignee_object_id=None, scope=None, assignee_principal_type=None, item_type=None, item=None, assignment_id=None):
    params = get_params(locals())   
    command = "az synapse role assignment create " + params
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

def list(workspace_name, role=None, assignee=None, assignee_object_id=None, scope=None, item=None, item_type=None):
    params = get_params(locals())   
    command = "az synapse role assignment list " + params
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

def show(workspace_name, id):
    params = get_params(locals())   
    command = "az synapse role assignment show " + params
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

def delete(workspace_name, ids=None, assignee=None, assignee_object_id=None, role=None, scope=None, item=None, item_type=None, yes=None):
    params = get_params(locals())   
    command = "az synapse role assignment delete " + params
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
