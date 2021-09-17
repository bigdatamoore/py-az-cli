import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def show(account, database_name, schema_name, table_name, partition_name):
    params = get_params(locals())   
    command = "az dla catalog table-partition show " + params
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

def list(account, database_name, schema_name, table_name, filter=None, top=None, skip=None, select=None, orderby=None, count=None):
    params = get_params(locals())   
    command = "az dla catalog table-partition list " + params
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
