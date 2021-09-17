import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, webapp_name, slot=None):
    params = get_params(locals())   
    command = "az webapp config backup list " + params
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

def show(resource_group, webapp_name, slot=None):
    params = get_params(locals())   
    command = "az webapp config backup show " + params
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

def create(resource_group, webapp_name, container_url, db_name=None, db_type=None, db_connection_string=None, backup_name=None, slot=None):
    params = get_params(locals())   
    command = "az webapp config backup create " + params
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

def update(resource_group, webapp_name, container_url=None, frequency=None, retain_one=None, retention=None, db_name=None, db_connection_string=None, db_type=None, backup_name=None, slot=None):
    params = get_params(locals())   
    command = "az webapp config backup update " + params
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

def restore(resource_group, webapp_name, container_url, backup_name, db_name=None, db_type=None, db_connection_string=None, target_name=None, overwrite=None, ignore_hostname_conflict=None, slot=None):
    params = get_params(locals())   
    command = "az webapp config backup restore " + params
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
