import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def build(registry, image, builder, pack_image_tag=None, agent_pool=None, pull=None, no_format=None, no_logs=None, timeout=None, resource_group=None, platform=None, auth_mode=None, no_wait=None):
    params = get_params(locals())   
    command = "az acr pack build " + params
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
