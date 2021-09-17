import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def create(resource_group, circuit_name, peering_type, peer_asn, vlan_id, primary_peer_subnet, secondary_peer_subnet, shared_key=None, advertised_public_prefixes=None, customer_asn=None, routing_registry_name=None, route_filter=None, legacy_mode=None, ip_version=None):
    params = get_params(locals())   
    command = "az network express-route peering create " + params
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

def delete(resource_group, circuit_name, name):
    params = get_params(locals())   
    command = "az network express-route peering delete " + params
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

def show(resource_group, circuit_name, name):
    params = get_params(locals())   
    command = "az network express-route peering show " + params
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

def list(resource_group, circuit_name):
    params = get_params(locals())   
    command = "az network express-route peering list " + params
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

def get_stats(resource_group, circuit_name, name):
    params = get_params(locals())   
    command = "az network express-route peering get-stats " + params
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

def update(resource_group, circuit_name, name, peer_asn=None, primary_peer_subnet=None, secondary_peer_subnet=None, vlan_id=None, shared_key=None, advertised_public_prefixes=None, customer_asn=None, routing_registry_name=None, route_filter=None, ip_version=None, legacy_mode=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "az network express-route peering update " + params
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
