import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def create(resource_group, name=None, hsm_name=None, administrators=None, location=None, sku=None, enabled_for_deployment=None, enabled_for_disk_encryption=None, enabled_for_template_deployment=None, enable_rbac_authorization=None, enable_soft_delete=None, enable_purge_protection=None, retention_days=None, network_acls=None, network_acls_ips=None, network_acls_vnets=None, bypass=None, default_action=None, no_self_perms=None, tags=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault create " + params
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

def recover(resource_group=None, location=None, name=None, hsm_name=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault recover " + params
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

def list(resource_group=None, resource_type=None):
    params = get_params(locals())   
    command = "az keyvault list " + params
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

def show(resource_group=None, name=None, hsm_name=None):
    params = get_params(locals())   
    command = "az keyvault show " + params
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

def delete(resource_group=None, name=None, hsm_name=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault delete " + params
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

def purge(location=None, name=None, hsm_name=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault purge " + params
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

def set_policy(resource_group=None, name, object_id=None, application_id=None, spn=None, upn=None, key_permissions=None, secret_permissions=None, certificate_permissions=None, storage_permissions=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault set-policy " + params
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

def delete_policy(resource_group=None, name, object_id=None, application_id=None, spn=None, upn=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault delete-policy " + params
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

def list_deleted(resource_type=None):
    params = get_params(locals())   
    command = "az keyvault list-deleted " + params
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

def show_deleted(location=None, name=None, hsm_name=None):
    params = get_params(locals())   
    command = "az keyvault show-deleted " + params
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

def update(resource_group=None, name, enabled_for_deployment=None, enabled_for_disk_encryption=None, enabled_for_template_deployment=None, enable_rbac_authorization=None, enable_soft_delete=None, enable_purge_protection=None, retention_days=None, bypass=None, default_action=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault update " + params
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

def wait(resource_group=None, name, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az keyvault wait " + params
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

def update_hsm(resource_group=None, hsm_name, enable_purge_protection=None, bypass=None, default_action=None, secondary_locations=None, set=None, add=None, remove=None, force_string=None, no_wait=None):
    params = get_params(locals())   
    command = "az keyvault update-hsm " + params
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

def wait_hsm(hsm_name, resource_group=None, timeout=None, interval=None, deleted=None, created=None, updated=None, exists=None, custom=None):
    params = get_params(locals())   
    command = "az keyvault wait-hsm " + params
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
