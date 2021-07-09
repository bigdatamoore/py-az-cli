import subprocess
from test.pyaz import get_params

def check_name(name):
    params = get_params(locals())   
    command = "acr check-name " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def list(resource_group=None):
    params = get_params(locals())   
    command = "acr list " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def create(name, resource_group, sku, location=None, admin_enabled=None, default_action=None, workspace=None, identity=None, key_encryption_key=None, public_network_enabled=None, zone_redundancy=None, allow_trusted_services=None, tags=None):
    params = get_params(locals())   
    command = "acr create " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def delete(name, resource_group=None, yes=None):
    params = get_params(locals())   
    command = "acr delete " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def show(name, resource_group=None):
    params = get_params(locals())   
    command = "acr show " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def show_usage(name, resource_group=None):
    params = get_params(locals())   
    command = "acr show-usage " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def show_endpoints(name, resource_group=None):
    params = get_params(locals())   
    command = "acr show-endpoints " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def update(name, resource_group=None, sku=None, admin_enabled=None, default_action=None, data_endpoint_enabled=None, public_network_enabled=None, allow_trusted_services=None, anonymous_pull_enabled=None, tags=None, set=None, add=None, remove=None, force_string=None):
    params = get_params(locals())   
    command = "acr update " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def login(name, resource_group=None, suffix=None, username=None, password=None, expose_token=None):
    params = get_params(locals())   
    command = "acr login " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def import_(name, source, registry=None, username=None, password=None, image=None, resource_group=None, repository=None, force=None):
    params = get_params(locals())   
    command = "acr import " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def build(registry, image=None, resource_group=None, agent_pool=None, timeout=None, build_arg=None, secret_build_arg=None, file=None, no_format=None, no_push=None, no_logs=None, platform=None, target=None, auth_mode=None, log_template=None, no_wait=None):
    params = get_params(locals())   
    command = "acr build " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def run(registry, agent_pool=None, file=None, values=None, set=None, set_secret=None, no_format=None, no_logs=None, timeout=None, resource_group=None, platform=None, auth_mode=None, log_template=None, no_wait=None):
    params = get_params(locals())   
    command = "acr run " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    

def check_health(ignore_errors=None, yes=None, name=None):
    params = get_params(locals())   
    command = "acr check-health " + params
    print(command)
    output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout =  output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    if stdout:
        print(stdout)
    else:
        print(stderr)    
