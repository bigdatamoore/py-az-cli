import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def create(properties, resource_group=None, namespace=None, parent=None, resource_type=None, name=None, id=None, api_version=None, location=None, is_full_object=None, latest_include_preview=None):
    params = get_params(locals())   
    command = "az resource create " + params
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

def delete(ids=None, resource_group=None, namespace=None, parent=None, resource_type=None, name=None, api_version=None, latest_include_preview=None):
    params = get_params(locals())   
    command = "az resource delete " + params
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

def show(ids=None, resource_group=None, namespace=None, parent=None, resource_type=None, name=None, api_version=None, include_response_body=None, latest_include_preview=None):
    params = get_params(locals())   
    command = "az resource show " + params
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

def list(resource_group=None, namespace=None, resource_type=None, name=None, tag=None, location=None):
    params = get_params(locals())   
    command = "az resource list " + params
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

def tag(tags, ids=None, resource_group=None, namespace=None, parent=None, resource_type=None, name=None, api_version=None, is_incremental=None, latest_include_preview=None):
    params = get_params(locals())   
    command = "az resource tag " + params
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

def move(ids, destination_group, destination_subscription_id=None):
    params = get_params(locals())   
    command = "az resource move " + params
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

def invoke_action(action, request_body=None, ids=None, resource_group=None, namespace=None, parent=None, resource_type=None, name=None, api_version=None, latest_include_preview=None):
    params = get_params(locals())   
    command = "az resource invoke-action " + params
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

def update(ids=None, resource_group=None, namespace=None, parent=None, resource_type=None, name=None, api_version=None, include_response_body=None, latest_include_preview=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az resource update " + params
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

def wait(ids=None, resource_group=None, namespace=None, parent=None, resource_type=None, name=None, api_version=None, include_response_body=None, __LATEST_INCLUDE_PREVIEW=None, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az resource wait " + params
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
