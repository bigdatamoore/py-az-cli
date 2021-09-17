import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, namespace_name, name, message_retention=None, partition_count=None, status=None, enable_capture=None, skip_empty_archives=None, capture_interval=None, capture_size_limit=None, destination_name=None, storage_account=None, blob_container=None, archive_name_format=None):
    params = get_params(locals())   
    command = "az eventhubs eventhub create " + params
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

def show(resource_group, namespace_name, name):
    params = get_params(locals())   
    command = "az eventhubs eventhub show " + params
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

def list(resource_group, namespace_name, skip=None, top=None):
    params = get_params(locals())   
    command = "az eventhubs eventhub list " + params
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

def delete(resource_group, namespace_name, name):
    params = get_params(locals())   
    command = "az eventhubs eventhub delete " + params
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

def update(resource_group, namespace_name, name, message_retention=None, partition_count=None, status=None, enable_capture=None, skip_empty_archives=None, capture_interval=None, capture_size_limit=None, destination_name=None, storage_account=None, blob_container=None, archive_name_format=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az eventhubs eventhub update " + params
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
