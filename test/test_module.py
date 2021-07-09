import pyaz.acr as acr
import subprocess

acr.list(resource_group="myrg")

# command = "az --version"
# output = subprocess.run(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
# stdout =  output.stdout.decode("utf-8")
# stderr = output.stderr.decode("utf-8")

# print(stdout)
