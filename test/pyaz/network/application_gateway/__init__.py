import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(name, resource_group, location=None, tags=None, capacity=None, cert_file=None, cert_password=None, key_vault_secret_id=None, frontend_port=None, http_settings_cookie_based_affinity=None, http_settings_port=None, http_settings_protocol=None, routing_rule_type=None, servers=None, sku=None, private_ip_address=None, public_ip_address=None, public_ip_address_allocation=None, subnet=None, subnet_address_prefix=None, vnet_name=None, vnet_address_prefix=None, __PUBLIC_IP_ADDRESS_TYPE=None, __SUBNET_TYPE=None, validate=None, connection_draining_timeout=None, http2=None, min_capacity=None, zones=None, custom_error_pages=None, waf_policy=None, max_capacity=None, identity=None, enable_private_link=None, private_link_ip_address=None, private_link_subnet=None, private_link_subnet_prefix=None, private_link_primary=None, trusted_client_cert=None, ssl_profile=None, ssl_profile_id=None, ssl_certificate_name=None, no_wait=None):
    params = get_params(locals())   
    command = "az network application-gateway create " + params
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
    command = "az network application-gateway delete " + params
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
    command = "az network application-gateway show " + params
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
    command = "az network application-gateway list " + params
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

def start(resource_group, name):
    params = get_params(locals())   
    command = "az network application-gateway start " + params
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

def stop(resource_group, name):
    params = get_params(locals())   
    command = "az network application-gateway stop " + params
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

def show_backend_health(resource_group, name, expand=None, protocol=None, host=None, path=None, timeout=None, host_name_from_http_settings=None, match_body=None, match_status_codes=None, address_pool=None, http_settings=None):
    params = get_params(locals())   
    command = "az network application-gateway show-backend-health " + params
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

def update(resource_group, name, sku=None, capacity=None, tags=None, http2=None, min_capacity=None, custom_error_pages=None, max_capacity=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az network application-gateway update " + params
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
    command = "az network application-gateway wait " + params
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
