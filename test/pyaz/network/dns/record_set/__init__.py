import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, zone_name, record_type=None):
    params = get_params(locals())   
    command = "az network dns record-set list " + params
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
