import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(resource_group, partner_namespace_name, name):
    params = get_params(locals())   
    command = "az eventgrid partner namespace event-channel show " + params
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

def delete(resource_group, partner_namespace_name, name, yes=None):
    params = get_params(locals())   
    command = "az eventgrid partner namespace event-channel delete " + params
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

def list(resource_group, partner_namespace_name, odata_query=None):
    params = get_params(locals())   
    command = "az eventgrid partner namespace event-channel list " + params
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

def create(resource_group, partner_namespace_name, name, source, destination_subscription_id, destination_resource_group_name, destination_topic_name, activation_expiration_date=None, partner_topic_description=None, publisher_filter=None):
    params = get_params(locals())   
    command = "az eventgrid partner namespace event-channel create " + params
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
