import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(disk_encryption_targets=None, image=None, id=None, vm_size=None, os_family=None, os_version=None, publisher=None, offer=None, sku=None, version=None, virtual_machine_image_id=None, node_agent_sku_id=None, targets=None, policy=None, resize_timeout=None, target_dedicated_nodes=None, target_low_priority_nodes=None, auto_scale_formula=None, enable_inter_node_communication=None, start_task_command_line=None, start_task_resource_files=None, start_task_wait_for_success=None, certificate_references=None, application_package_references=None, application_licenses=None, task_slots_per_node=None, metadata=None, json_file=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch pool create " + params
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

def list(filter=None, select=None, expand=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch pool list " + params
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

def delete(pool_id, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, yes=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch pool delete " + params
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

def show(pool_id, select=None, expand=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch pool show " + params
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

def set(pool_id, start_task_command_line=None, start_task_resource_files=None, start_task_environment_settings=None, start_task_max_task_retry_count=None, start_task_wait_for_success=None, certificate_references=None, application_package_references=None, metadata=None, json_file=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch pool set " + params
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

def reset(account_name=None, account_key=None, account_endpoint=None, pool_id, json_file=None, start_task_command_line=None, certificate_references=None, application_package_references=None, metadata=None, start_task_environment_settings=None, start_task_wait_for_success=None, start_task_max_task_retry_count=None):
    params = get_params(locals())   
    command = "az batch pool reset " + params
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

def resize(account_name=None, account_key=None, account_endpoint=None, pool_id, target_dedicated_nodes=None, target_low_priority_nodes=None, resize_timeout=None, node_deallocation_option=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, abort=None):
    params = get_params(locals())   
    command = "az batch pool resize " + params
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
