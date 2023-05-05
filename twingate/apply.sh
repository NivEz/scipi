#!/bin/bash

# export all env variables
set -o allexport
source cli/.env.tf_vars

docker build -t terraform:scipi .

docker run --name terraform --volume $(pwd)/terraform:/home/terraform_files terraform:scipi init
return_code=$?
docker rm terraform > /dev/null 2>&1
if [ $return_code -ne 0 ]
then
  exit $return_code
fi

docker run --name terraform --volume $(pwd)/terraform:/home/terraform_files terraform:scipi apply -auto-approve
return_code=$?
docker rm terraform > /dev/null 2>&1
if [ $return_code -ne 0 ]
then
  exit $return_code
fi
