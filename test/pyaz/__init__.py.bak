def get_cli_name(name: str) -> str:
    """
    converts name back to cli format from pythonic version
    - strips trailing underscore from keywords
    - converts remaining underscores to dashes
    - adds leading dashes
    """
    if name[-1] == "_":
        name = name[0:-1]
    name = name.replace("_","-")
    name = f"--{name}"
    return name

def get_params(params):
    #return params
    output = []
    
    for param in params:
        output.append(f"{get_cli_name(param)} '{params[param]}'")    
    
    return " ".join(output)



