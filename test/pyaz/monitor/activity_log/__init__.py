import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(filters=None, correlation_id=None, resource_group=None, resource_id=None, namespace=None, start_time=None, end_time=None, caller=None, status=None, max_events=None, select=None, offset=None):
    params = get_params(locals())   
    command = "az monitor activity-log list " + params
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

def list_categories():
    params = get_params(locals())   
    command = "az monitor activity-log list-categories " + params
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
