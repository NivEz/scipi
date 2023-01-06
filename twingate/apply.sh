#!/bin/bash

docker build -t terraform .

docker run --name terraform --volume $(pwd)/terraform:/home/terraform_files terraform init
docker rm terraform > /dev/null 2>&1

docker run --name terraform --volume $(pwd)/terraform:/home/terraform_files terraform apply -auto-approve
docker rm terraform > /dev/null 2>&1

