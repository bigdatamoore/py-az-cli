import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group, cluster_name, application):
    params = get_params(locals())   
    command = "az sf managed-service list " + params
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

def delete(resource_group, cluster_name, application, name):
    params = get_params(locals())   
    command = "az sf managed-service delete " + params
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

def show(resource_group, cluster_name, application, name):
    params = get_params(locals())   
    command = "az sf managed-service show " + params
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

def create(resource_group, cluster_name, application, name, type, state, default_move_cost=None, placement_constraints=None, service_package_activation_mode=None, target_replica_set_size=None, min_replica_set_size=None, has_persisted_state=None, service_placement_time_limit=None, stand_by_replica_keep_duration=None, quorum_loss_wait_duration=None, replica_restart_wait_duration=None, instance_count=None, min_instance_count=None, min_instance_percentage=None, partition_scheme=None, partition_count=None, low_key=None, high_key=None, partition_names=None, tags=None):
    params = get_params(locals())   
    command = "az sf managed-service create " + params
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

def update(resource_group, cluster_name, application, name, default_move_cost=None, placement_constraints=None, target_replica_set_size=None, min_replica_set_size=None, service_placement_time_limit=None, stand_by_replica_keep_duration=None, quorum_loss_wait_duration=None, replica_restart_wait_duration=None, instance_count=None, min_instance_count=None, min_instance_percentage=None, tags=None):
    params = get_params(locals())   
    command = "az sf managed-service update " + params
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
