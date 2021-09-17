import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, name):
    params = get_params(locals())   
    command = "az eventhubs cluster namespace list " + params
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
