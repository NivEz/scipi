FROM alpine:latest

RUN apk add --no-cache terraform

WORKDIR /home/terraform_files

ARG TF_VAR_twingate_network
ARG TF_VAR_twingate_remote_network
ARG TF_VAR_twingate_resource_name
ARG TF_VAR_twingate_api_token
ARG TF_VAR_ip_address

ENV TF_VAR_twingate_network=$TF_VAR_twingate_network
ENV TF_VAR_twingate_remote_network=$TF_VAR_twingate_remote_network
ENV TF_VAR_twingate_resource_name=$TF_VAR_twingate_resource_name
ENV TF_VAR_twingate_api_token=$TF_VAR_twingate_api_token
ENV TF_VAR_ip_address=$TF_VAR_ip_address

ENTRYPOINT ["terraform"]
