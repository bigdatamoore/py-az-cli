import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(pool_id, node_id, account_name=None, account_key=None, account_endpoint=None):
    params = get_params(locals())   
    command = "az batch node remote-login-settings show " + params
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
