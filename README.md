# ONOS Cluster Docker
This repository help you to create ONOS cluster in single machine with Docker.

## Installation
- Install python3 and python3-pip
- Install Docker & Docker Compose
- Edit variable
```
nano configuration_variable.yaml
```
- Install requirement
```
pip3 install -r requirement.txt
```
- Generate configuration
```
python3 generate_config.py
```
- Run docker compose
```
docker-compose up -d
```
- Get ONOS IP address
```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' onos-1
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' onos-2
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' onos-3
```

