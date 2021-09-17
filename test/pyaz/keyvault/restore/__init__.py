import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def start(id=None, storage_resource_uri=None, storage_account_name=None, blob_container_name=None, storage_container_SAS_token, backup_folder, hsm_name=None):
    params = get_params(locals())   
    command = "az keyvault restore start " + params
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
