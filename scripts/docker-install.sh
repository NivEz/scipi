#!/bin/bash

me=$(whoami)

if [ $me == 'root' ]
then
  echo Do not execute as root!
  exit 1
fi

check_if_docker_installed () {
  docker ps > /dev/null 2>&1
  return_code=$?
  if [ $return_code -eq 0 ]
  then
    echo Docker is already installed on you machine
    exit 0
  fi
}

check_if_docker_installed

# Install docker
curl -sSL https://get.docker.com | sh

# Run docker as non-root user
sudo usermod -aG docker $me

# Start docker service
sudo systemctl start docker

# Check if docker works
docker ps > /dev/null 2>&1
return_code=$?
if [ $return_code -ne 0 ]
then
  sudo su $me
  docker ps > /dev/null 2>&1
  return_code=$?
  if [ $return_code -ne 0 ]
  then
    echo Installed docker properly!
    exit 1
  fi
fi
