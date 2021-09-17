import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(resource_group, namespace_name, topic_name, name, lock_duration=None, enable_session=None, default_message_time_to_live=None, enable_dead_lettering_on_message_expiration=None, max_delivery_count=None, status=None, enable_batched_operations=None, auto_delete_on_idle=None, forward_to=None, forward_dead_lettered_messages_to=None, dead_letter_on_filter_exceptions=None):
    params = get_params(locals())   
    command = "az servicebus topic subscription create " + params
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

def show(resource_group, namespace_name, topic_name, name):
    params = get_params(locals())   
    command = "az servicebus topic subscription show " + params
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

def list(resource_group, namespace_name, topic_name, skip=None, top=None):
    params = get_params(locals())   
    command = "az servicebus topic subscription list " + params
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

def delete(resource_group, namespace_name, topic_name, name):
    params = get_params(locals())   
    command = "az servicebus topic subscription delete " + params
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

def update(resource_group, namespace_name, topic_name, name, lock_duration=None, enable_session=None, default_message_time_to_live=None, enable_dead_lettering_on_message_expiration=None, max_delivery_count=None, status=None, enable_batched_operations=None, auto_delete_on_idle=None, forward_to=None, forward_dead_lettered_messages_to=None, dead_letter_on_filter_exceptions=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az servicebus topic subscription update " + params
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
