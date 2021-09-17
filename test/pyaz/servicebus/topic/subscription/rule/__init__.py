import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def create(resource_group, namespace_name, topic_name, subscription_name, name, action_sql_expression=None, action_compatibility_level=None, enable_action_preprocessing=None, filter_sql_expression=None, enable_sql_preprocessing=None, correlation_id=None, message_id=None, to=None, reply_to=None, label=None, session_id=None, reply_to_session_id=None, content_type=None, enable_correlation_preprocessing=None):
    params = get_params(locals())   
    command = "az servicebus topic subscription rule create " + params
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

def show(resource_group, namespace_name, topic_name, subscription_name, name):
    params = get_params(locals())   
    command = "az servicebus topic subscription rule show " + params
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

def list(resource_group, namespace_name, topic_name, subscription_name, skip=None, top=None):
    params = get_params(locals())   
    command = "az servicebus topic subscription rule list " + params
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

def delete(resource_group, namespace_name, topic_name, subscription_name, name):
    params = get_params(locals())   
    command = "az servicebus topic subscription rule delete " + params
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

def update(resource_group, namespace_name, topic_name, subscription_name, name, action_sql_expression=None, action_compatibility_level=None, enable_action_preprocessing=None, filter_sql_expression=None, enable_sql_preprocessing=None, correlation_id=None, message_id=None, to=None, reply_to=None, label=None, session_id=None, reply_to_session_id=None, content_type=None, enable_correlation_preprocessing=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az servicebus topic subscription rule update " + params
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
