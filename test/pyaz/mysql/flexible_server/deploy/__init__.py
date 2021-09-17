import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def setup(resource_group, server_name, database_name, admin_user, admin_password, sql_file, repo, action_name=None, branch=None, allow_push=None):
    params = get_params(locals())   
    command = "az mysql flexible-server deploy setup " + params
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

def run(action_name, branch):
    params = get_params(locals())   
    command = "az mysql flexible-server deploy run " + params
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
