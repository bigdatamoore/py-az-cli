import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(name, top=None, resource_group=None, suffix=None, username=None, password=None):
    params = get_params(locals())   
    command = "az acr repository list " + params
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

def show_tags(name, repository, top=None, orderby=None, resource_group=None, suffix=None, username=None, password=None, detail=None):
    params = get_params(locals())   
    command = "az acr repository show-tags " + params
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

def show_manifests(name, repository, top=None, orderby=None, resource_group=None, suffix=None, username=None, password=None, detail=None):
    params = get_params(locals())   
    command = "az acr repository show-manifests " + params
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

def show(name, repository=None, image=None, resource_group=None, suffix=None, username=None, password=None):
    params = get_params(locals())   
    command = "az acr repository show " + params
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

def update(name, repository=None, image=None, resource_group=None, suffix=None, username=None, password=None, delete_enabled=None, list_enabled=None, read_enabled=None, write_enabled=None):
    params = get_params(locals())   
    command = "az acr repository update " + params
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

def delete(name, repository=None, image=None, resource_group=None, suffix=None, username=None, password=None, yes=None):
    params = get_params(locals())   
    command = "az acr repository delete " + params
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

def untag(name, image, resource_group=None, suffix=None, username=None, password=None):
    params = get_params(locals())   
    command = "az acr repository untag " + params
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
