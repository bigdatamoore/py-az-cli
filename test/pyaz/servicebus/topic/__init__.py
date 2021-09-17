import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, namespace_name, name, default_message_time_to_live=None, max_size=None, enable_duplicate_detection=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, status=None, enable_ordering=None, auto_delete_on_idle=None, enable_partitioning=None, enable_express=None):
    params = get_params(locals())   
    command = "az servicebus topic create " + params
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
    command = "az servicebus topic show " + params
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
    command = "az servicebus topic list " + params
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
    command = "az servicebus topic delete " + params
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

def update(resource_group, namespace_name, name, default_message_time_to_live=None, max_size=None, enable_duplicate_detection=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, status=None, enable_ordering=None, auto_delete_on_idle=None, enable_partitioning=None, enable_express=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az servicebus topic update " + params
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
