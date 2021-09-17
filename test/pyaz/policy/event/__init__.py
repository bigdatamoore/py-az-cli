import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(management_group=None, resource_group=None, resource=None, namespace=None, parent=None, resource_type=None, policy_set_definition=None, policy_definition=None, policy_assignment=None, from_=None, to=None, order_by=None, select=None, top=None, filter=None, apply=None):
    params = get_params(locals())   
    command = "az policy event list " + params
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
