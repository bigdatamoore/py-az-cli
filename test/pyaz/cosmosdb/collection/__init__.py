import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group_name=None, name=None, key=None, url_connection=None, db_name, collection_name):
    params = get_params(locals())   
    command = "az cosmosdb collection show " + params
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

def list(resource_group_name=None, name=None, key=None, url_connection=None, db_name):
    params = get_params(locals())   
    command = "az cosmosdb collection list " + params
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

def exists(resource_group_name=None, name=None, key=None, url_connection=None, db_name, collection_name):
    params = get_params(locals())   
    command = "az cosmosdb collection exists " + params
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

def create(resource_group_name=None, name=None, key=None, url_connection=None, db_name, collection_name, throughput=None, partition_key_path=None, default_ttl=None, indexing_policy=None):
    params = get_params(locals())   
    command = "az cosmosdb collection create " + params
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

def delete(resource_group_name=None, name=None, key=None, url_connection=None, db_name, collection_name, yes=None):
    params = get_params(locals())   
    command = "az cosmosdb collection delete " + params
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

def update(resource_group_name=None, name=None, key=None, url_connection=None, db_name, collection_name, throughput=None, default_ttl=None, indexing_policy=None):
    params = get_params(locals())   
    command = "az cosmosdb collection update " + params
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
