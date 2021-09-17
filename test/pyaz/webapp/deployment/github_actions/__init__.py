import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, name, repo, runtime=None, token=None, slot=None, branch=None, login_with_github=None, force=None):
    params = get_params(locals())   
    command = "az webapp deployment github-actions add " + params
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

def remove(resource_group, name, repo, token=None, slot=None, branch=None, login_with_github=None):
    params = get_params(locals())   
    command = "az webapp deployment github-actions remove " + params
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
