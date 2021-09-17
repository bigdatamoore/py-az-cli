import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group=None):
    params = get_params(locals())   
    command = "az sf managed-cluster list " + params
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

def delete(resource_group, cluster_name):
    params = get_params(locals())   
    command = "az sf managed-cluster delete " + params
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

def show(resource_group, cluster_name):
    params = get_params(locals())   
    command = "az sf managed-cluster show " + params
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

def create(resource_group, cluster_name, admin_password, admin_user_name=None, dns_name=None, location=None, sku=None, client_connection_port=None, gateway_connection_port=None, client_cert_is_admin=None, client_cert_thumbprint=None, client_cert_common_name=None, client_cert_issuer_thumbprint=None, cluster_upgrade_mode=None, cluster_upgrade_cadence=None, cluster_code_version=None, tags=None):
    params = get_params(locals())   
    command = "az sf managed-cluster create " + params
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

def update(resource_group, cluster_name, client_connection_port=None, gateway_connection_port=None, dns_name=None, tags=None):
    params = get_params(locals())   
    command = "az sf managed-cluster update " + params
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
