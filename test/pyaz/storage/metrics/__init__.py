import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def update(account_name=None, account_key=None, connection_string=None, sas_token=None, services, retention, hour=None, minute=None, api=None, timeout=None):
    params = get_params(locals())   
    command = "az storage metrics update " + params
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

def show(account_name=None, account_key=None, connection_string=None, sas_token=None, services=None, interval=None, timeout=None):
    params = get_params(locals())   
    command = "az storage metrics show " + params
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
