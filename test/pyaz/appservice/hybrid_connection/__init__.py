import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def set_key(plan, resource_group, namespace, hybrid_connection, key_type):
    params = get_params(locals())   
    command = "az appservice hybrid-connection set-key " + params
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
