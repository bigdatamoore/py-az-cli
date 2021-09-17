"""
Utility functions for the pyaz generated code to use
"""

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

def get_params(locals):
    """
    given the built-in locals dictionary returns a formatted string
    with the az cli formatted parameter names and values in a comma-separated list
    """
    #return params
    output = []
    
    # loop through locals and append list of parameters and their values
    # as long as the parameter has a value
    for param in locals:
        if locals[param]:
            output.append(f"{get_cli_name(param)} '{locals[param]}'")    
    
    return " ".join(output)



