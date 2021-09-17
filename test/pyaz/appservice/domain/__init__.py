import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, hostname, contact_info, privacy=None, auto_renew=None, accept_terms=None, tags=None, dryrun=None):
    params = get_params(locals())   
    command = "az appservice domain create " + params
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

def show_terms(hostname):
    params = get_params(locals())   
    command = "az appservice domain show-terms " + params
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
