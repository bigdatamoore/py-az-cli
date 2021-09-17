import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def browse(name, resource_group, disable_browser=None, ssh_key_file=None):
    params = get_params(locals())   
    command = "az acs kubernetes browse " + params
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

def get_credentials(name, resource_group, file=None, ssh_key_file=None, overwrite_existing=None):
    params = get_params(locals())   
    command = "az acs kubernetes get-credentials " + params
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

def install_cli(client_version=None, install_location=None, base_src_url=None, kubelogin_version=None, kubelogin_install_location=None, kubelogin_base_src_url=None):
    params = get_params(locals())   
    command = "az acs kubernetes install-cli " + params
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
