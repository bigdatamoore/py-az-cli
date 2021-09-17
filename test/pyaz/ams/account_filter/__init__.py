import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(account_name, resource_group, name, start_timestamp=None, end_timestamp=None, presentation_window_duration=None, live_backoff_duration=None, timescale=None, force_end_timestamp=None, bitrate=None, first_quality=None, tracks=None):
    params = get_params(locals())   
    command = "az ams account-filter create " + params
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

def show(resource_group, account_name, name):
    params = get_params(locals())   
    command = "az ams account-filter show " + params
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
    command = "az ams account-filter list " + params
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

def delete(resource_group, account_name, name):
    params = get_params(locals())   
    command = "az ams account-filter delete " + params
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

def update(resource_group, account_name, name, start_timestamp=None, end_timestamp=None, presentation_window_duration=None, live_backoff_duration=None, timescale=None, bitrate=None, first_quality=None, tracks=None, force_end_timestamp=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az ams account-filter update " + params
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
