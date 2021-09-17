import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def submit(account, job_name, script, runtime_version=None, compile_mode=None, compile_only=None, degree_of_parallelism=None, priority=None, recurrence_id=None, recurrence_name=None, pipeline_id=None, pipeline_name=None, pipeline_uri=None, run_id=None):
    params = get_params(locals())   
    command = "az dla job submit " + params
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

def wait(account, job_id, wait_interval_sec=None, max_wait_time_sec=None):
    params = get_params(locals())   
    command = "az dla job wait " + params
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

def show(account, job_identity):
    params = get_params(locals())   
    command = "az dla job show " + params
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

def cancel(account, job_identity):
    params = get_params(locals())   
    command = "az dla job cancel " + params
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

def list(account, top=None, name=None, submitter=None, submitted_after=None, submitted_before=None, state=None, result=None, pipeline_id=None, recurrence_id=None):
    params = get_params(locals())   
    command = "az dla job list " + params
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
