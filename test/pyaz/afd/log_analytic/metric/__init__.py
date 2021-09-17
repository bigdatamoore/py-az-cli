import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def list(resource_group, profile_name, metrics, date_time_begin, date_time_end, granularity, custom_domains, protocols, group_by=None, continents=None, country_or_regions=None):
    params = get_params(locals())   
    command = "az afd log-analytic metric list " + params
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
