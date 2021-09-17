import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def set(resource_group, name, slot=None, number_of_workers=None, linux_fx_version=None, __WINDOWS_FX_VERSION=None, prewarmed_instance_count=None, php_version=None, python_version=None, net_framework_version=None, java_version=None, java_container=None, java_container_version=None, remote_debugging_enabled=None, web_sockets_enabled=None, always_on=None, auto_heal_enabled=None, use_32bit_worker_process=None, min_tls_version=None, http20_enabled=None, startup_file=None, ftps_state=None, vnet_route_all_enabled=None, generic_configurations=None):
    params = get_params(locals())   
    command = "az functionapp config set " + params
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

def show(resource_group, name, slot=None):
    params = get_params(locals())   
    command = "az functionapp config show " + params
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
