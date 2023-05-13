#!/bin/bash

chmod +x ./apply.sh
./apply.sh

return_code=$?
if [ $return_code -ne 0 ]
then
  exit $return_code
fi

# export all env variables
set -o allexport
source ../cli/.env.tf_vars
source terraform/.env.tokens

docker run -d --sysctl net.ipv4.ping_group_range="0 2147483647" \
--env TENANT_URL="https://$TF_VAR_twingate_network.twingate.com" \
--env ACCESS_TOKEN="$ACCESS_TOKEN" \
--env REFRESH_TOKEN="$REFRESH_TOKEN" \
--env TWINGATE_LABEL_HOSTNAME="`hostname`" \
--name "twingate-scipi" \
--restart=unless-stopped \
$(docker run --help | grep -- --pull >/dev/null && echo "--pull=always") twingate/connector:1
