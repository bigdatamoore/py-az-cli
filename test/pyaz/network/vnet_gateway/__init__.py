import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(resource_group, name, public_ip_addresses, vnet, location=None, tags=None, gateway_type=None, sku=None, vpn_type=None, vpn_gateway_generation=None, asn=None, bgp_peering_address=None, peer_weight=None, address_prefixes=None, radius_server=None, radius_secret=None, client_protocol=None, gateway_default_site=None, custom_routes=None, aad_tenant=None, aad_audience=None, aad_issuer=None, root_cert_data=None, root_cert_name=None, vpn_auth_type=None, edge_zone=None, nat_rule=None, no_wait=None):
    params = get_params(locals())   
    command = "az network vnet-gateway create " + params
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

def update(address_prefixes=None, resource_group, name, sku=None, vpn_type=None, tags=None, public_ip_addresses=None, gateway_type=None, enable_bgp=None, asn=None, bgp_peering_address=None, peer_weight=None, vnet=None, radius_server=None, radius_secret=None, client_protocol=None, gateway_default_site=None, custom_routes=None, aad_tenant=None, aad_audience=None, aad_issuer=None, root_cert_data=None, root_cert_name=None, vpn_auth_type=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az network vnet-gateway update " + params
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

def wait(resource_group, name, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az network vnet-gateway wait " + params
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

def delete(resource_group, name, no_wait=None):
    params = get_params(locals())   
    command = "az network vnet-gateway delete " + params
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

def show(resource_group, name):
    params = get_params(locals())   
    command = "az network vnet-gateway show " + params
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

def list(resource_group):
    params = get_params(locals())   
    command = "az network vnet-gateway list " + params
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

def reset(resource_group, name, gateway_vip=None):
    params = get_params(locals())   
    command = "az network vnet-gateway reset " + params
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

def list_bgp_peer_status(resource_group, name, peer=None):
    params = get_params(locals())   
    command = "az network vnet-gateway list-bgp-peer-status " + params
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

def list_advertised_routes(resource_group, name, peer):
    params = get_params(locals())   
    command = "az network vnet-gateway list-advertised-routes " + params
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

def list_learned_routes(resource_group, name):
    params = get_params(locals())   
    command = "az network vnet-gateway list-learned-routes " + params
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

def show_supported_devices(resource_group, name):
    params = get_params(locals())   
    command = "az network vnet-gateway show-supported-devices " + params
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

def disconnect_vpn_connections(resource_group, name, vpn_connections, no_wait=None):
    params = get_params(locals())   
    command = "az network vnet-gateway disconnect-vpn-connections " + params
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
