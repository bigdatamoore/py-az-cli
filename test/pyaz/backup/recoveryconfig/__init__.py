import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, vault_name, restore_mode, container_name, item_name, rp_name=None, target_item_name=None, log_point_in_time=None, target_server_type=None, target_server_name=None, workload_type=None, backup_management_type=None, from_full_rp_name=None, filepath=None, target_container_name=None):
    params = get_params(locals())   
    command = "az backup recoveryconfig show " + params
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
