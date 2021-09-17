import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(display_name, homepage=None, identifier_uris=None, available_to_other_tenants=None, password=None, reply_urls=None, key_value=None, key_type=None, key_usage=None, start_date=None, end_date=None, oauth2_allow_implicit_flow=None, required_resource_accesses=None, native_app=None, credential_description=None, app_roles=None, optional_claims=None):
    params = get_params(locals())   
    command = "az ad app create " + params
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

def delete(id):
    params = get_params(locals())   
    command = "az ad app delete " + params
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

def list(app_id=None, display_name=None, identifier_uri=None, filter=None, all=None, show_mine=None):
    params = get_params(locals())   
    command = "az ad app list " + params
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

def show(id):
    params = get_params(locals())   
    command = "az ad app show " + params
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

def update(id, display_name=None, homepage=None, identifier_uris=None, password=None, reply_urls=None, key_value=None, key_type=None, key_usage=None, start_date=None, end_date=None, available_to_other_tenants=None, oauth2_allow_implicit_flow=None, required_resource_accesses=None, credential_description=None, app_roles=None, optional_claims=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az ad app update " + params
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
