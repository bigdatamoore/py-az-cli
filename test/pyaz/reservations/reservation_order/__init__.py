import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list():
    params = get_params(locals())   
    command = "az reservations reservation-order list " + params
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

def show(reservation_order_id, expand=None):
    params = get_params(locals())   
    command = "az reservations reservation-order show " + params
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

def calculate(sku, reserved_resource_type, billing_scope, term, quantity, applied_scope_type, display_name, applied_scope=None, renew=None, instance_flexibility=None, location=None, billing_plan=None):
    params = get_params(locals())   
    command = "az reservations reservation-order calculate " + params
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

def purchase(reservation_order_id, sku, reserved_resource_type, billing_scope, term, quantity, applied_scope_type, display_name, applied_scope=None, renew=None, instance_flexibility=None, location=None, billing_plan=None):
    params = get_params(locals())   
    command = "az reservations reservation-order purchase " + params
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
