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
- Generate configuration
```
python3 generate_config.py
```
- Run docker compose
```
docker-compose up -d
```
