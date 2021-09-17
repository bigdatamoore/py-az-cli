import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(resource_group, account_name, snapshot_policy_name):
    params = get_params(locals())   
    command = "az netappfiles snapshot policy show " + params
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

def list(resource_group, account_name):
    params = get_params(locals())   
    command = "az netappfiles snapshot policy list " + params
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

def volumes(resource_group, account_name, snapshot_policy_name):
    params = get_params(locals())   
    command = "az netappfiles snapshot policy volumes " + params
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

def delete(resource_group, account_name, snapshot_policy_name):
    params = get_params(locals())   
    command = "az netappfiles snapshot policy delete " + params
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

def update(resource_group, account_name, snapshot_policy_name, location, hourly_snapshots=None, hourly_minute=None, daily_snapshots=None, daily_minute=None, daily_hour=None, weekly_snapshots=None, weekly_minute=None, weekly_hour=None, weekly_day=None, monthly_snapshots=None, monthly_minute=None, monthly_hour=None, monthly_days=None, enabled=None):
    params = get_params(locals())   
    command = "az netappfiles snapshot policy update " + params
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

def create(resource_group, account_name, snapshot_policy_name, location, hourly_snapshots=None, hourly_minute=None, daily_snapshots=None, daily_minute=None, daily_hour=None, weekly_snapshots=None, weekly_minute=None, weekly_hour=None, weekly_day=None, monthly_snapshots=None, monthly_minute=None, monthly_hour=None, monthly_days=None, enabled=None, tags=None):
    params = get_params(locals())   
    command = "az netappfiles snapshot policy create " + params
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
