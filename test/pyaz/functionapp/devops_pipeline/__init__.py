import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def create(functionapp_name=None, organization_name=None, project_name=None, repository_name=None, overwrite_yaml=None, allow_force_push=None, github_pat=None, github_repository=None):
    params = get_params(locals())   
    command = "az functionapp devops-pipeline create " + params
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
