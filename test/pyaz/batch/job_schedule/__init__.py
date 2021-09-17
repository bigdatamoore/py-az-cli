import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(do_not_run_until=None, do_not_run_after=None, start_window=None, recurrence_interval=None, priority=None, max_parallel_tasks=None, uses_task_dependencies=None, on_all_tasks_complete=None, job_max_wall_clock_time=None, job_max_task_retry_count=None, id=None, job_manager_task_id=None, job_manager_task_command_line=None, job_manager_task_resource_files=None, required_slots=None, pool_id=None, metadata=None, json_file=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job-schedule create " + params
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

def delete(job_schedule_id, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, yes=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job-schedule delete " + params
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

def show(job_schedule_id, select=None, expand=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job-schedule show " + params
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

def set(job_schedule_id, do_not_run_until=None, do_not_run_after=None, start_window=None, recurrence_interval=None, priority=None, max_parallel_tasks=None, uses_task_dependencies=None, on_all_tasks_complete=None, job_manager_task_id=None, job_manager_task_command_line=None, job_manager_task_resource_files=None, job_manager_task_environment_settings=None, required_slots=None, job_manager_task_application_package_references=None, pool_id=None, job_metadata=None, metadata=None, json_file=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job-schedule set " + params
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

def reset(job_schedule_id, do_not_run_until=None, do_not_run_after=None, start_window=None, recurrence_interval=None, priority=None, max_parallel_tasks=None, uses_task_dependencies=None, on_all_tasks_complete=None, job_manager_task_id=None, job_manager_task_command_line=None, job_manager_task_resource_files=None, job_manager_task_environment_settings=None, required_slots=None, job_manager_task_application_package_references=None, pool_id=None, job_metadata=None, metadata=None, json_file=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job-schedule reset " + params
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

def disable(job_schedule_id, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job-schedule disable " + params
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

def enable(job_schedule_id, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job-schedule enable " + params
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

def stop(job_schedule_id, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch job-schedule stop " + params
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
    command = "az batch job-schedule list " + params
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
