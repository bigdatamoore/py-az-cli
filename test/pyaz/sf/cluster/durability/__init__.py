import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def update(resource_group, cluster_name, node_type, durability_level):
    params = get_params(locals())   
    command = "az sf cluster durability update " + params
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
