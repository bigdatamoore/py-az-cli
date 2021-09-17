import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group, filter=None):
    params = get_params(locals())   
    command = "az deployment group list " + params
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

def show(resource_group, name):
    params = get_params(locals())   
    command = "az deployment group show " + params
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

def delete(resource_group, name, no_wait=None):
    params = get_params(locals())   
    command = "az deployment group delete " + params
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

def validate(resource_group, template_file=None, template_uri=None, parameters=None, name=None, mode=None, rollback_on_error=None, handle_extended_json_format=None, no_prompt=None, template_spec=None, query_string=None):
    params = get_params(locals())   
    command = "az deployment group validate " + params
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

def create(resource_group, template_file=None, template_uri=None, parameters=None, name=None, mode=None, rollback_on_error=None, handle_extended_json_format=None, aux_subs=None, aux_tenants=None, no_prompt=None, confirm_with_what_if=None, what_if_result_format=None, what_if_exclude_change_types=None, template_spec=None, query_string=None, what_if=None, proceed_if_no_change=None, no_wait=None):
    params = get_params(locals())   
    command = "az deployment group create " + params
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

def what_if(resource_group, template_file=None, template_uri=None, parameters=None, name=None, mode=None, aux_tenants=None, result_format=None, no_pretty_print=None, no_prompt=None, exclude_change_types=None, template_spec=None, query_string=None):
    params = get_params(locals())   
    command = "az deployment group what-if " + params
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

def export(resource_group, name):
    params = get_params(locals())   
    command = "az deployment group export " + params
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

def wait(resource_group, name, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az deployment group wait " + params
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

def cancel(resource_group, name):
    params = get_params(locals())   
    command = "az deployment group cancel " + params
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
