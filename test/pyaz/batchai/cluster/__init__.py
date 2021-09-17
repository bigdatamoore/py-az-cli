import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, workspace, name, config_file=None, user_name=None, ssh_key=None, password=None, generate_ssh_keys=None, image=None, custom_image=None, use_auto_storage=None, vm_size=None, vm_priority=None, target=None, min=None, max=None, subnet=None, nfs=None, nfs_mount_path=None, afs_name=None, afs_mount_path=None, bfs_name=None, bfs_mount_path=None, storage_account_name=None, storage_account_key=None, setup_task=None, setup_task_output=None):
    params = get_params(locals())   
    command = "az batchai cluster create " + params
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

def delete(resource_group, workspace, name, yes=None, no_wait=None):
    params = get_params(locals())   
    command = "az batchai cluster delete " + params
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

def show(resource_group, workspace, name):
    params = get_params(locals())   
    command = "az batchai cluster show " + params
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

def list(resource_group, workspace):
    params = get_params(locals())   
    command = "az batchai cluster list " + params
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

def resize(resource_group, workspace, name, target):
    params = get_params(locals())   
    command = "az batchai cluster resize " + params
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

def auto_scale(resource_group, workspace, name, min, max):
    params = get_params(locals())   
    command = "az batchai cluster auto-scale " + params
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
