import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_group, system_topic_name, name, include_full_endpoint_url=None, include_static_delivery_attribute_secret=None):
    params = get_params(locals())   
    command = "az eventgrid system-topic event-subscription show " + params
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

def delete(resource_group, system_topic_name, name, yes=None):
    params = get_params(locals())   
    command = "az eventgrid system-topic event-subscription delete " + params
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

def list(resource_group, system_topic_name, odata_query=None):
    params = get_params(locals())   
    command = "az eventgrid system-topic event-subscription list " + params
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

def create(resource_group, system_topic_name, name, endpoint=None, endpoint_type=None, included_event_types=None, subject_begins_with=None, subject_ends_with=None, subject_case_sensitive=None, max_delivery_attempts=None, event_ttl=None, max_events_per_batch=None, preferred_batch_size_in_kilobytes=None, event_delivery_schema=None, deadletter_endpoint=None, labels=None, expiration_date=None, advanced_filter=None, azure_active_directory_tenant_id=None, azure_active_directory_application_id_or_uri=None, storage_queue_msg_ttl=None, enable_advanced_filtering_on_arrays=None, delivery_attribute_mapping=None):
    params = get_params(locals())   
    command = "az eventgrid system-topic event-subscription create " + params
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

def update(resource_group, system_topic_name, name, endpoint=None, endpoint_type=None, subject_begins_with=None, subject_ends_with=None, included_event_types=None, advanced_filter=None, labels=None, deadletter_endpoint=None, storage_queue_msg_ttl=None, enable_advanced_filtering_on_arrays=None, delivery_attribute_mapping=None):
    params = get_params(locals())   
    command = "az eventgrid system-topic event-subscription update " + params
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
