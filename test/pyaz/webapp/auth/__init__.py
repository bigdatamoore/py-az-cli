import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(resource_group, name, slot=None):
    params = get_params(locals())   
    command = "az webapp auth show " + params
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

def update(resource_group, name, enabled=None, action=None, aad_client_id=None, token_store=None, runtime_version=None, token_refresh_extension_hours=None, allowed_external_redirect_urls=None, aad_client_secret=None, aad_client_secret_certificate_thumbprint=None, aad_allowed_token_audiences=None, aad_token_issuer_url=None, facebook_app_id=None, facebook_app_secret=None, facebook_oauth_scopes=None, twitter_consumer_key=None, twitter_consumer_secret=None, google_client_id=None, google_client_secret=None, google_oauth_scopes=None, microsoft_account_client_id=None, microsoft_account_client_secret=None, microsoft_account_oauth_scopes=None, slot=None):
    params = get_params(locals())   
    command = "az webapp auth update " + params
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
