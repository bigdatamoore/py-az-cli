import json, subprocess
from ... pyaz_utils import get_cli_name, get_params


def show(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, container_name, timeout=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, tags_condition=None, snapshot=None, lease_id=None):
    params = get_params(locals())   
    command = "az storage blob show " + params
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

def set_tier(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, container_name, timeout=None, tier, type=None, rehydrate_priority=None):
    params = get_params(locals())   
    command = "az storage blob set-tier " + params
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

def list(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, timeout=None, delimiter=None, include=None, marker=None, num_results=None, prefix=None, show_next_marker=None):
    params = get_params(locals())   
    command = "az storage blob list " + params
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

def query(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, container_name, timeout=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, tags_condition=None, lease_id=None, input_format=None, output_format=None, in_line_separator=None, in_column_separator=None, in_quote_char=None, in_record_separator=None, in_escape_char=None, in_has_header=None, out_line_separator=None, out_column_separator=None, out_quote_char=None, out_record_separator=None, out_escape_char=None, out_has_header=None, result_file=None, query_expression, __INPUT_CONFIG=None, __OUTPUT_CONFIG=None):
    params = get_params(locals())   
    command = "az storage blob query " + params
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

def rewrite(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, name, container_name, timeout=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, tags_condition=None, lease_id=None, tier=None, encryption_scope=None, source_uri):
    params = get_params(locals())   
    command = "az storage blob rewrite " + params
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

def download(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, no_progress=None, socket_timeout=None, container_name, name, file, open_mode=None, snapshot=None, start_range=None, end_range=None, validate_content=None, __PROGRESS_CALLBACK=None, max_connections=None, lease_id=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob download " + params
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

def generate_sas(account_name=None, account_key=None, connection_string=None, __SAS_TOKEN=None, auth_mode=None, container_name, name, permissions=None, expiry=None, start=None, policy_name=None, ip=None, https_only=None, cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, full_uri=None, as_user=None):
    params = get_params(locals())   
    command = "az storage blob generate-sas " + params
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

def url(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, name, protocol=None, snapshot=None):
    params = get_params(locals())   
    command = "az storage blob url " + params
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

def snapshot(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, name, metadata=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, lease_id=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob snapshot " + params
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

def update(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, clear_content_settings=None, container_name, name, __CONTENT_SETTINGS=None, lease_id=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob update " + params
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

def exists(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, name, snapshot=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob exists " + params
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

def delete(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, name, snapshot=None, lease_id=None, delete_snapshots=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, timeout=None):
    params = get_params(locals())   
    command = "az storage blob delete " + params
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

def undelete(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container_name, name, timeout=None):
    params = get_params(locals())   
    command = "az storage blob undelete " + params
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

def upload(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, name, container_name, timeout=None, no_progress=None, socket_timeout=None, file, type=None, __CONTENT_SETTINGS=None, metadata=None, validate_content=None, maxsize_condition=None, max_connections=None, lease_id=None, tier=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, __PROGRESS_CALLBACK=None, encryption_scope=None):
    params = get_params(locals())   
    command = "az storage blob upload " + params
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

def upload_batch(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, content_type=None, content_encoding=None, content_language=None, content_disposition=None, content_cache_control=None, content_md5=None, no_progress=None, socket_timeout=None, source, destination, pattern=None, __SOURCE_FILES=None, destination_path=None, __DESTINATION_CONTAINER_NAME=None, type=None, __CONTENT_SETTINGS=None, metadata=None, validate_content=None, maxsize_condition=None, max_connections=None, lease_id=None, __PROGRESS_CALLBACK=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, timeout=None, dryrun=None):
    params = get_params(locals())   
    command = "az storage blob upload-batch " + params
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

def download_batch(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, no_progress=None, socket_timeout=None, source, destination, __SOURCE_CONTAINER_NAME=None, pattern=None, dryrun=None, __PROGRESS_CALLBACK=None, max_connections=None):
    params = get_params(locals())   
    command = "az storage blob download-batch " + params
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

def delete_batch(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, source, __SOURCE_CONTAINER_NAME=None, pattern=None, lease_id=None, delete_snapshots=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, timeout=None, dryrun=None):
    params = get_params(locals())   
    command = "az storage blob delete-batch " + params
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

def restore(resource_group=None, account_name, time_to_restore, blob_range=None, no_wait=None):
    params = get_params(locals())   
    command = "az storage blob restore " + params
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

def sync(account_name=None, account_key=None, connection_string=None, sas_token=None, auth_mode=None, container, destination=None, source, __DESTINATION=None, exclude_pattern=None, include_pattern=None, exclude_path=None):
    params = get_params(locals())   
    command = "az storage blob sync " + params
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
