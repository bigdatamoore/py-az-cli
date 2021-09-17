import json, subprocess
from ..... pyaz_utils import get_cli_name, get_params


def create(type, aggregation, metric, operator, namespace=None, dimension=None, threshold=None, sensitivity=None, num_periods=None, num_violations=None, since=None):
    params = get_params(locals())   
    command = "az monitor metrics alert condition create " + params
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
