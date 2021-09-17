import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def browse(name, resource_group, disable_browser=None, ssh_key_file=None):
    params = get_params(locals())   
    command = "az acs dcos browse " + params
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

def install_cli(install_location=None, client_version=None):
    params = get_params(locals())   
    command = "az acs dcos install-cli " + params
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
