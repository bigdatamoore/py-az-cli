import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def show(vm_resource_id, workspace_id, server_name, database_name, scan_id, rule_id, vm_name=None, agent_id=None, vm_uuid=None):
    params = get_params(locals())   
    command = "az security va sql results show " + params
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

def list(vm_resource_id, workspace_id, server_name, database_name, scan_id, vm_name=None, agent_id=None, vm_uuid=None):
    params = get_params(locals())   
    command = "az security va sql results list " + params
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
