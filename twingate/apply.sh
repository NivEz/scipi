#!/bin/bash

# export all env variables
set -o allexport
source ../cli/.env.tf_vars

docker build -t terraform:scipi \
  --build-arg TF_VAR_twingate_network="$TF_VAR_twingate_network" \
  --build-arg TF_VAR_twingate_remote_network="$TF_VAR_twingate_remote_network" \
  --build-arg TF_VAR_twingate_resource_name="$TF_VAR_twingate_resource_name" \
  --build-arg TF_VAR_twingate_api_token="$TF_VAR_twingate_api_token" \
  --build-arg TF_VAR_ip_address="$TF_VAR_ip_address" .

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
