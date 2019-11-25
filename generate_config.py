import yaml
from jinja2 import Environment, FileSystemLoader

# set current directory
ENV = Environment(loader=FileSystemLoader('.'))

# Get configuration variable
with open("configuration_variable.yaml") as y:
    configuration = yaml.load(y)

#########################################
##### Generate atomix configuration #####
#########################################

for data in configuration["atomix"]:

    # get template
    baseline = ENV.get_template("./template-configuration/atomix/atomix.conf.j2")

    # create file
    file = open('./configuration/atomix/%s.conf' %data["hostname"], 'w')

    # create config
    config = baseline.render(node=data, atomix=configuration["atomix"])

    file.write(config)
    file.close

#######################################
##### Generate onos configuration #####
#######################################

for data in configuration["onos"]:

    # get template
    baseline = ENV.get_template("./template-configuration/onos/cluster.json.j2")

    # create file
    file = open('./configuration/onos/%s.json' %data["hostname"], 'w')

    # create config
    config = baseline.render(node=data, atomix=configuration["atomix"])

    file.write(config)
    file.close

#################################################
##### Generate docker compose configuration #####
#################################################

# get template
baseline = ENV.get_template("./template-configuration/docker-compose.yaml.j2")

# create file
file = open('./docker-compose.yaml', 'w')

# create config
config = baseline.render(data=configuration, atomix=configuration["atomix"], onos=configuration["onos"])

file.write(config)
file.close