import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def update(account_name, profile_name=None, customer_name=None, marketplace_purchases=None, reservation_purchases=None, view_charges=None):
    params = get_params(locals())   
    command = "az billing policy update " + params
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

def show(account_name, profile_name=None, customer_name=None):
    params = get_params(locals())   
    command = "az billing policy show " + params
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
