import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group, cluster_name):
    params = get_params(locals())   
    command = "az sf managed-application list " + params
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

def delete(resource_group, cluster_name, name):
    params = get_params(locals())   
    command = "az sf managed-application delete " + params
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

def show(resource_group, cluster_name, name):
    params = get_params(locals())   
    command = "az sf managed-application show " + params
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

def create(resource_group, cluster_name, type_name, version, name, package_url=None, parameters=None, tags=None):
    params = get_params(locals())   
    command = "az sf managed-application create " + params
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

def update(resource_group, cluster_name, name, version=None, parameters=None, force_restart=None, recreate_application=None, upgrade_replica_set_check_timeout=None, instance_close_delay_duration=None, failure_action=None, upgrade_mode=None, hc_retry_timeout=None, hc_wait_duration=None, hc_stable_duration=None, ud_timeout=None, upgrade_timeout=None, warning_as_error=None, max_percent_unhealthy_partitions=None, max_percent_unhealthy_replicas=None, max_percent_unhealthy_services=None, max_percent_unhealthy_deployed_applications=None, service_type_health_policy_map=None, tags=None):
    params = get_params(locals())   
    command = "az sf managed-application update " + params
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
