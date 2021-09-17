import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def delete(pool_id, node_list=None, resize_timeout=None, node_deallocation_option=None, json_file=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node delete " + params
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

def show(pool_id, node_id, select=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node show " + params
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

def list(pool_id, filter=None, select=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node list " + params
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

def reboot(pool_id, node_id, node_reboot_option=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node reboot " + params
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

def reimage(pool_id, node_id, node_reimage_option=None, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node reimage " + params
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
