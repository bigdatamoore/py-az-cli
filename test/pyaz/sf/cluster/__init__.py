import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, cluster_name):
    params = get_params(locals())   
    command = "az sf cluster show " + params
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

def list(resource_group=None):
    params = get_params(locals())   
    command = "az sf cluster list " + params
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

def create(resource_group, location=None, certificate_subject_name=None, parameter_file=None, template_file=None, cluster_name=None, vault_rg=None, vault_name=None, certificate_file=None, certificate_password=None, certificate_output_folder=None, secret_identifier=None, vm_user_name=None, vm_password=None, cluster_size=None, vm_sku=None, vm_os=None):
    params = get_params(locals())   
    command = "az sf cluster create " + params
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
