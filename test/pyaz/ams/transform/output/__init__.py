import json, subprocess
from .... pyaz_utils import get_cli_name, get_params


def add(account_name, resource_group, name, preset, insights_to_extract=None, video_analysis_mode=None, audio_language=None, audio_analysis_mode=None, on_error=None, relative_priority=None, resolution=None):
    params = get_params(locals())   
    command = "az ams transform output add " + params
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

def remove(account_name, resource_group, name, output_index):
    params = get_params(locals())   
    command = "az ams transform output remove " + params
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
