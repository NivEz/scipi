#!/bin/bash

curl -sSL https://raw.githubusercontent.com/NivEz/my-snippets/main/docker-install.sh | sh

return_code=$?
if [ $return_code -ne 0 ]
then
  exit $return_code
fi
