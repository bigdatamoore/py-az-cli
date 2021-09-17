import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(resource_group, cluster_name, is_admin=None, thumbprint=None, certificate_common_name=None, certificate_issuer_thumbprint=None, admin_client_thumbprints=None, readonly_client_thumbprints=None, client_certificate_common_names=None):
    params = get_params(locals())   
    command = "az sf cluster client-certificate add " + params
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

def remove(resource_group, cluster_name, thumbprints=None, certificate_common_name=None, certificate_issuer_thumbprint=None, client_certificate_common_names=None):
    params = get_params(locals())   
    command = "az sf cluster client-certificate remove " + params
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
