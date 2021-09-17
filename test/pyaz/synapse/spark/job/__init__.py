import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def submit(workspace_name, spark_pool_name, name, main_definition_file, main_class_name, executor_size, executors, language=None, arguments=None, reference_files=None, archives=None, configuration=None, tags=None):
    params = get_params(locals())   
    command = "az synapse spark job submit " + params
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

def list(workspace_name, spark_pool_name, from_index=None, size=None):
    params = get_params(locals())   
    command = "az synapse spark job list " + params
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

def show(livy_id, workspace_name, spark_pool_name):
    params = get_params(locals())   
    command = "az synapse spark job show " + params
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

def cancel(livy_id, workspace_name, spark_pool_name, yes=None):
    params = get_params(locals())   
    command = "az synapse spark job cancel " + params
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
