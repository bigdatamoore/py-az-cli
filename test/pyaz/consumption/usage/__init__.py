import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def list(billing_period_name=None, top=None, include_additional_properties=None, include_meter_details=None, start_date=None, end_date=None):
    params = get_params(locals())   
    command = "az consumption usage list " + params
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
