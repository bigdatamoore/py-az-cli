import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def query_by_pipeline_run(workspace_name, name, run_id, last_updated_after, last_updated_before, continuation_token=None, filters=None, order_by=None):
    params = get_params(locals())   
    command = "az synapse activity-run query-by-pipeline-run " + params
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
