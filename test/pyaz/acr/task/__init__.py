import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(name, registry, context=None, agent_pool=None, file=None, git_access_token=None, image=None, status=None, platform=None, cpu=None, timeout=None, values=None, source_trigger_name=None, commit_trigger_enabled=None, pull_request_trigger_enabled=None, schedule=None, no_push=None, no_cache=None, arg=None, secret_arg=None, set=None, set_secret=None, base_image_trigger_name=None, base_image_trigger_enabled=None, base_image_trigger_type=None, update_trigger_endpoint=None, update_trigger_payload_type=None, resource_group=None, assign_identity=None, target=None, auth_mode=None, log_template=None, is_system_task=None):
    params = get_params(locals())   
    command = "az acr task create " + params
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

def show(name, registry, with_secure_properties=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr task show " + params
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

def list(registry, resource_group=None):
    params = get_params(locals())   
    command = "az acr task list " + params
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

def delete(name, registry, resource_group=None, yes=None):
    params = get_params(locals())   
    command = "az acr task delete " + params
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

def update(name, registry, resource_group=None, agent_pool=None, status=None, platform=None, cpu=None, timeout=None, context=None, commit_trigger_enabled=None, pull_request_trigger_enabled=None, git_access_token=None, image=None, no_push=None, no_cache=None, file=None, values=None, arg=None, secret_arg=None, set=None, set_secret=None, base_image_trigger_enabled=None, base_image_trigger_type=None, update_trigger_endpoint=None, update_trigger_payload_type=None, target=None, auth_mode=None, log_template=None):
    params = get_params(locals())   
    command = "az acr task update " + params
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

def run(name, registry, agent_pool=None, set=None, set_secret=None, file=None, context=None, arg=None, secret_arg=None, target=None, update_trigger_token=None, no_logs=None, resource_group=None, log_template=None, no_wait=None):
    params = get_params(locals())   
    command = "az acr task run " + params
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

def list_runs(registry, top=None, name=None, run_status=None, image=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr task list-runs " + params
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

def show_run(run_id, registry, resource_group=None):
    params = get_params(locals())   
    command = "az acr task show-run " + params
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

def cancel_run(run_id, registry, resource_group=None):
    params = get_params(locals())   
    command = "az acr task cancel-run " + params
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

def update_run(run_id, registry, no_archive=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr task update-run " + params
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

def logs(registry, run_id=None, name=None, image=None, resource_group=None):
    params = get_params(locals())   
    command = "az acr task logs " + params
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
