"""
Module to generate code for az-cli-py
"""
import os
import tooling
import json
import keyword


class Constants:
    COMMAND_ROOT = "pyaz"  # the root name of the command path


def pythonize_name(name: str) -> str:
    """
    given a name, makes it pythonic
    - removes leading dashes
    - replaces remaining dashes with underscores
    - checks for keywords and appends a trailing underscore
    """
    name = name.replace("--","").replace("-","_")
    if name in keyword.kwlist:
        name = name + "_"
    return name

def get_commands():
    """
    returns a dictionary with all the az cli commands, keyed by the path to the command
    inside each dictionary entry is another dictionary of verbs for that command 
    with the command object (from cli core module) being stored in that
    """    

    # using Microsoft VSCode tooling module to load the az cli command table 
    tooling.initialize()
    commands = tooling.load_command_table()

    command_dict = {} # initialize empty dict for our return 

    # iterate through the all the commands
    for command_name in commands:
        command = commands[command_name]
        #print(command_name)                # get the name of the command in format "az ..."
        command_list = command_name.split(" ")          # split apart each command segment
        command_list = [pythonize_name(name) for name in command_list]      # pythonize the names
        command_verb = command_list.pop()               # remove the last command which is the action verb
        command_path = os.path.join(Constants.COMMAND_ROOT, *command_list)  # build path of commands 
        
        # add command path to dictionary if not already there
        if command_path not in command_dict:
            command_dict[command_path]={}

        # add the command object to the dictionary using the path and verb as keys
        command_dict[command_path][command_verb] = command
    
    return command_dict


def generate_code(base_dir):
    """
    creates a folder structure starting from the base_dir based on the hierarchy of 
    the commands, with a folder for each command containing an __init__ module
    that contains the "verb" functions (if any) associated with that command
    """    
    commands = get_commands()

    for command_path in commands:
        print(f"generating code module for: {command_path}")
        
        # get the module path and create it if it doesn't exist
        module_dir = os.path.join(base_dir, command_path)
        os.makedirs(name=module_dir, exist_ok=True)

        # create the module __init__ file that will contain the verb functions
        with open(f"{module_dir}/__init__.py", mode="w") as f:

            # get the level of depth for this command based on the path separator
            # add one so that the top-most is level 1
            command_depth = command_path.count(os.path.sep) + 1

            # create import_dots to represent level of depth for importing the pyaz_utils
            import_dots = "." * command_depth

            # write the imports to the top of each module
            f.write("import json, subprocess\n")
            f.write(f"from {import_dots} pyaz_utils import get_cli_name, get_params\n\n")

            # for each command verb write a function with a boiler plate format
            for command_verb in commands[command_path]:

                # placeholder list for the output arguments
                output_args = []

                # get the command object from the command table
                command = commands[command_path][command_verb]

                # get the dictionary of arguments for the command
                arguments = tooling.get_arguments(command)

                # loop through each argument in the arguments dictionary
                for argument in arguments:

                    # get the argument object
                    arg = arguments[argument]

                    # get the options_list which is the options for this argument in the format:
                    # ['--resource-group', '-g']
                    options_list = arg.type.settings.get("options_list",[])

                    # if there are options then derive the argument name from the options
                    if len(options_list) > 0:

                        # remove any non strings from options_list 
                        # when testing, found one option with an object of type knack.deprecation.Deprecated object
                        options_list = [option for option in options_list if isinstance(option, str)]

                        # get the first option from the options list as that is the one we want
                        # the second option is the shorter one
                        # and pythonize the name of the argument
                        output_arg = pythonize_name(options_list[0])

                        # get the argument's help text
                        help = arg.type.settings.get("help","")

                        # get the argument's default value
                        default = arg.type.settings.get("default",None)

                        # get whether the argument is required
                        required = arg.type.settings.get("required",False)

                        # append =None to the argument output in case it is not required
                        if not required:
                            output_arg = output_arg + "=None"

                        # strip out these default cmd arguments which are not applicable
                        # and add the output arguments to a list
                        if output_arg not in ["__cmd__=None","cmd=None"]:
                            output_args.append(output_arg)
                
                # take the output arguments list and format it as a comma-separated string
                arguments_formatted = ", ".join(output_args)

                # write the command verb's function body using the parts 
                # to the command's __init__ module
                f.write(
f"""
def {command_verb}({arguments_formatted}):
    params = get_params(locals())   
    command = "az {command.name} " + params
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
""")


    
if __name__=="__main__":
    # get path to the current file's directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # set up test dir where to create code
    test_dir = os.path.join(current_dir,"test")
    
    # call function to generate the code in the test dir
    generate_code(test_dir)


