import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(resource_group, server_name, filename_contains=None, file_last_written=None, max_file_size=None):
    params = get_params(locals())   
    command = "az mariadb server-logs list " + params
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

def download(resource_group, server_name, name):
    params = get_params(locals())   
    command = "az mariadb server-logs download " + params
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
