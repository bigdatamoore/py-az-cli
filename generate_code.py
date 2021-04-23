"""
Module to generate code for az-cli-py
"""
import os
import tooling
import json
import keyword


class CommandGroup:
    """Represents a group of commands"""
    def __init__(self, name):
        self.name = name
        self.commands = {}
        self.subgroups = {}

    # def __repr__(self):
    #     return (f'{self.__class__.__name__}('
    #             f'name=\'{self.name}\','
    #             f'commands={self.commands},'
    #             f'subgroups={self.subgroups})'
    #             )

    def __repr__(self):
        out = {}
        out["name"]= self.name
        out["commands"]=self.commands
        out["subgroups"]=self.subgroups
        return str(out)


class Command:
    """Represents a cli command"""
    def __init__(self, name, help=""):
        self.name = name
        self.help = help 

    # def __repr__(self):
    #     return (f'{self.__class__.__name__}('
    #             f'name=\'{self.name}\')')        

    def __repr__(self):
        out = {}
        out["name"]= self.name
        return str(out)

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

def get_commands2(command_dict):
    tooling.initialize()
    commands = tooling.load_command_table()

    for command_name in commands:
        command = commands[command_name]
        command_name_new = "pyaz " + command_name
        command_list = command_name_new.split(" ")
        command_list = [pythonize_name(name) for name in command_list]
        command_verb = command_list.pop()
        command_path = "/".join(command_list)

        if command_path not in command_dict:
            command_dict[command_path]={}

        command_dict[command_path][command_verb] = command
    
    return command_dict


def get_commands(base_group):
    tooling.initialize()
    commands = tooling.load_command_table()

    #f = open(file="commands.txt", mode="w")
    for command_name in commands:

        #if command_name == "aks browse":
        #    break

        #print(command_name)
        command = commands[command_name]

        command_list = command_name.split(" ")

        group = base_group

        while len(command_list) > 0:

            original_name = command_list.pop(0)
            new_name = pythonize_name(original_name)
            
            if len(command_list) == 0:
                group.commands[new_name] = Command(new_name)
            else:
                if new_name not in group.subgroups:
                    new_group = CommandGroup(new_name)
                    group.subgroups[new_group.name] = new_group
                    group = new_group
                else:
                    group = group.subgroups[new_name]
    
    return base_group
            

        #print(base_group.subgroups)

        # arguments = tooling.get_arguments(command)
        # for argument_name in arguments:
        #     argument = arguments[argument_name]
        #     help = argument.type.settings.get('help','')
        #     required = argument.type.settings.get('required',False)
        #     default = argument.type.settings.get('default',None)
        #     options_list = argument.type.settings.get('options_list',[])

        #f.write(command + "\n")
        # parts = command.split(" ")
        # count = len(parts)

        # parts = [pythonize_name(part) for part in parts]

        # method = parts.pop()
        # module = parts.pop()

        # module_dir = "/".join(parts)
        # module_dir = f"{base_dir}/az/{module_dir}"
        # os.makedirs(name=module_dir, exist_ok=True)

        # with open(f"{module_dir}/{module}.py", mode="a") as f:
        #     f.write(f"def {method}():\n  pass\n\n\n")

    #f.close()
        

        # for i in range(count):
        #     part = split[i]

        #     if i == count-2:
        #         print(f"module: {part}")
        #     else if i == count-1:
        #         print(f"function: {}")
        #     else:
        
        #     print(split[i])


def main(base_dir):

    #az = CommandGroup("az")
    #commands = get_commands(az)
    
    commands = {}
    commands = get_commands2(commands)

    for command_path in commands:
        print(command_path)
        module_dir = base_dir + command_path
        os.makedirs(name=module_dir, exist_ok=True)

        with open(f"{module_dir}/__init__.py", mode="w") as f:
        #     f.write(f"def {method}():\n  pass\n\n\n")

            for command_verb in commands[command_path]:

                output_args = []
                command = commands[command_path][command_verb]
                arguments = tooling.get_arguments(command)
                for argument in arguments:
                    arg = arguments[argument]
                    options_list = arg.type.settings.get("options_list",[])
                    if len(options_list) > 0:
                        output_arg = pythonize_name(options_list[0])
                        help = arg.type.settings.get("help","")
                        default = arg.type.settings.get("default",None)
                        required = arg.type.settings.get("required",False)

                        if not required:
                            output_arg = output_arg + "=None"

                        if output_arg not in ["__cmd__=None","cmd=None"]:
                            output_args.append(output_arg)
                
                arguments_formatted = ", ".join(output_args)
                f.write(
f"""
def {command_verb}({arguments_formatted}):
    params = get_params(locals())   
    command = "{command.name} " + params
    print(command)
""")

            print("\t" + command_verb + ":" + commands[command_path][command_verb].name)
            break

    # with open("dump.json","w") as f:
    #     f.write(str(commands).replace("'",'"'))

    
    

if __name__=="__main__":
    # get path to the current file's directory
    #base_dir = os.path.dirname(os.path.realpath(__file__))
    #generate_modules(base_dir)
    
    base_dir = "/Users/david/Repos/az-py-cli/test/"
    main(base_dir)


    # cg = CommandGroup("az")
    # cg2 = CommandGroup("acr")
    # c = Command("check_name")
    # cg2.commands["check_name"] = c
    # cg.subgroups["acr"] = cg2
    # print(cg)


