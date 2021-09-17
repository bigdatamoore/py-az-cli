import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(name, resource_group=None, authentication_provider=None):
    params = get_params(locals())   
    command = "az staticwebapp users list " + params
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

def invite(name, authentication_provider, user_details, domain, roles, invitation_expiration_in_hours, resource_group=None):
    params = get_params(locals())   
    command = "az staticwebapp users invite " + params
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

def update(name, roles, authentication_provider=None, user_details=None, user_id=None, resource_group=None):
    params = get_params(locals())   
    command = "az staticwebapp users update " + params
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
