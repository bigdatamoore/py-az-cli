import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(priority=None, max_parallel_tasks=None, job_max_wall_clock_time=None, job_max_task_retry_count=None, id=None, job_manager_task_id=None, job_manager_task_command_line=None, job_manager_task_resource_files=None, job_manager_task_environment_settings=None, required_slots=None, pool_id=None, metadata=None, uses_task_dependencies=None, json_file=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job create " + params
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

def delete(job_id, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, yes=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job delete " + params
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

def show(job_id, select=None, expand=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job show " + params
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

def set(job_id, priority=None, max_parallel_tasks=None, on_all_tasks_complete=None, job_max_wall_clock_time=None, job_max_task_retry_count=None, pool_id=None, metadata=None, json_file=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job set " + params
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

def reset(job_id, priority=None, job_max_wall_clock_time=None, job_max_task_retry_count=None, pool_id=None, metadata=None, on_all_tasks_complete=None, json_file=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job reset " + params
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

def list(account_name=None, account_key=None, account_endpoint=None, job_schedule_id=None, filter=None, select=None, expand=None):
    params = get_params(locals())   
    command = "az batch job list " + params
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

def disable(job_id, disable_tasks=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job disable " + params
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

def enable(job_id, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job enable " + params
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

def stop(job_id, terminate_reason=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job stop " + params
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
