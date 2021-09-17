import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, profile_name, metrics, date_time_begin, date_time_end, max_ranking, rankings, actions=None, rule_types=None):
    params = get_params(locals())   
    command = "az afd waf-log-analytic ranking list " + params
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
