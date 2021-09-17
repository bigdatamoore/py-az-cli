import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def retrieve_latest_backup_time(resource_group, account_name, database_name, container_name, location):
    params = get_params(locals())   
    command = "az cosmosdb sql retrieve-latest-backup-time " + params
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
