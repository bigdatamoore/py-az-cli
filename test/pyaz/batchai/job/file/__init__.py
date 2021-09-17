import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, workspace, experiment, job, output_directory_id=None, path=None, expiry=None):
    params = get_params(locals())   
    command = "az batchai job file list " + params
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

def stream(resource_group, workspace, experiment, job, file_name, output_directory_id=None, path=None):
    params = get_params(locals())   
    command = "az batchai job file stream " + params
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
