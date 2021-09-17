import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(resource_group, account_name, name):
    params = get_params(locals())   
    command = "az cosmosdb cassandra keyspace throughput show " + params
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

def update(resource_group, account_name, name, throughput=None, max_throughput=None):
    params = get_params(locals())   
    command = "az cosmosdb cassandra keyspace throughput update " + params
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

def migrate(resource_group, account_name, name, throughput_type):
    params = get_params(locals())   
    command = "az cosmosdb cassandra keyspace throughput migrate " + params
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
