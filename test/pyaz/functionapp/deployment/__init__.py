import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list_publishing_profiles(resource_group, name, slot=None, xml=None):
    params = get_params(locals())   
    command = "az functionapp deployment list-publishing-profiles " + params
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

def list_publishing_credentials(resource_group, name, slot=None):
    params = get_params(locals())   
    command = "az functionapp deployment list-publishing-credentials " + params
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
