import json, subprocess
from .. pyaz_utils import get_cli_name, get_params


def list():
    params = get_params(locals())   
    command = "az cloud list " + params
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

def show(name=None):
    params = get_params(locals())   
    command = "az cloud show " + params
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

def register(name, cloud_config=None, profile=None, endpoint_management=None, endpoint_resource_manager=None, endpoint_sql_management=None, endpoint_gallery=None, endpoint_active_directory=None, endpoint_active_directory_resource_id=None, endpoint_active_directory_graph_resource_id=None, endpoint_active_directory_data_lake_resource_id=None, endpoint_vm_image_alias_doc=None, suffix_sql_server_hostname=None, suffix_storage_endpoint=None, suffix_keyvault_dns=None, suffix_azure_datalake_store_file_system_endpoint=None, suffix_azure_datalake_analytics_catalog_and_job_endpoint=None, suffix_acr_login_server_endpoint=None):
    params = get_params(locals())   
    command = "az cloud register " + params
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

def unregister(name):
    params = get_params(locals())   
    command = "az cloud unregister " + params
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

def set(name, profile=None):
    params = get_params(locals())   
    command = "az cloud set " + params
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

def update(name=None, cloud_config=None, profile=None, endpoint_management=None, endpoint_resource_manager=None, endpoint_sql_management=None, endpoint_gallery=None, endpoint_active_directory=None, endpoint_active_directory_resource_id=None, endpoint_active_directory_graph_resource_id=None, endpoint_active_directory_data_lake_resource_id=None, endpoint_vm_image_alias_doc=None, suffix_sql_server_hostname=None, suffix_storage_endpoint=None, suffix_keyvault_dns=None, suffix_azure_datalake_store_file_system_endpoint=None, suffix_azure_datalake_analytics_catalog_and_job_endpoint=None, suffix_acr_login_server_endpoint=None):
    params = get_params(locals())   
    command = "az cloud update " + params
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

def list_profiles(name=None, show_all=None):
    params = get_params(locals())   
    command = "az cloud list-profiles " + params
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
