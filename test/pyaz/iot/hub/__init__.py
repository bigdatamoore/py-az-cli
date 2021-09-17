import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(name, resource_group, location=None, sku=None, unit=None, partition_count=None, retention_day=None, c2d_ttl=None, c2d_max_delivery_count=None, disable_local_auth=None, disable_device_sas=None, disable_module_sas=None, feedback_lock_duration=None, feedback_ttl=None, feedback_max_delivery_count=None, fileupload_notifications=None, fileupload_notification_lock_duration=None, fileupload_notification_max_delivery_count=None, fileupload_notification_ttl=None, fileupload_storage_connectionstring=None, fileupload_storage_container_name=None, fileupload_sas_ttl=None, fileupload_storage_auth_type=None, fileupload_storage_container_uri=None, fileupload_storage_identity=None, min_tls_version=None, tags=None, mi_system_assigned=None, mi_user_assigned=None, role=None, scopes=None):
    params = get_params(locals())   
    command = "az iot hub create " + params
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

def list(resource_group=None):
    params = get_params(locals())   
    command = "az iot hub list " + params
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

def show_connection_string(hub_name=None, resource_group=None, policy_name=None, key=None, all=None):
    params = get_params(locals())   
    command = "az iot hub show-connection-string " + params
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

def show(name, resource_group=None):
    params = get_params(locals())   
    command = "az iot hub show " + params
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

def update(name, resource_group=None, sku=None, unit=None, retention_day=None, c2d_ttl=None, c2d_max_delivery_count=None, disable_local_auth=None, disable_device_sas=None, disable_module_sas=None, feedback_lock_duration=None, feedback_ttl=None, feedback_max_delivery_count=None, fileupload_notifications=None, fileupload_notification_lock_duration=None, fileupload_notification_max_delivery_count=None, fileupload_notification_ttl=None, fileupload_storage_connectionstring=None, fileupload_storage_container_name=None, fileupload_sas_ttl=None, fileupload_storage_auth_type=None, fileupload_storage_container_uri=None, fileupload_storage_identity=None, tags=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az iot hub update " + params
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

def delete(name, resource_group=None):
    params = get_params(locals())   
    command = "az iot hub delete " + params
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

def list_skus(name, resource_group=None):
    params = get_params(locals())   
    command = "az iot hub list-skus " + params
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

def show_quota_metrics(name, resource_group=None):
    params = get_params(locals())   
    command = "az iot hub show-quota-metrics " + params
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

def show_stats(name, resource_group=None):
    params = get_params(locals())   
    command = "az iot hub show-stats " + params
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

def manual_failover(name, resource_group=None, no_wait=None):
    params = get_params(locals())   
    command = "az iot hub manual-failover " + params
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
