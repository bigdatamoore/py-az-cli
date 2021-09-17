import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def import_(resource_group, service_name, path, specification_format, description=None, subscription_key_header_name=None, subscription_key_query_param_name=None, api_id=None, api_revision=None, api_version=None, api_version_set_id=None, display_name=None, service_url=None, protocols=None, specification_path=None, specification_url=None, api_type=None, subscription_required=None, soap_api_type=None, wsdl_endpoint_name=None, wsdl_service_name=None, no_wait=None):
    params = get_params(locals())   
    command = "az apim api import " + params
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

def create(resource_group, service_name, api_id, description=None, subscription_key_header_name=None, subscription_key_query_param_name=None, open_id_provider_id=None, bearer_token_sending_methods=None, authorization_server_id=None, authorization_scope=None, display_name, service_url=None, protocols=None, path, subscription_key_required=None, api_type=None, subscription_required=None, no_wait=None):
    params = get_params(locals())   
    command = "az apim api create " + params
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

def show(resource_group, service_name, api_id):
    params = get_params(locals())   
    command = "az apim api show " + params
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

def list(resource_group, service_name, filter_display_name=None, top=None, skip=None):
    params = get_params(locals())   
    command = "az apim api list " + params
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

def delete(resource_group, service_name, api_id, delete_revisions=None, if_match=None, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az apim api delete " + params
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

def update(resource_group, service_name, api_id, if_match=None, description=None, subscription_key_header_name=None, subscription_key_query_param_name=None, display_name=None, service_url=None, protocols=None, path=None, api_type=None, subscription_required=None, tags=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az apim api update " + params
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

def wait(resource_group, name, api_id, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az apim api wait " + params
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
