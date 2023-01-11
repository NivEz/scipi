terraform {
  required_providers {
    twingate = {
      source = "twingate/twingate"
    }
  }
}

provider "twingate" {
  api_token = var.twingate_api_token
  network   = var.twingate_network
}

resource "twingate_remote_network" "scipi_network" {
  name = var.twingate_remote_network
}

resource "twingate_connector" "scipi_connector" {
  remote_network_id = twingate_remote_network.scipi_network.id
}

resource "twingate_connector_tokens" "scipi_connector_tokens" {
  connector_id = twingate_connector.scipi_connector.id
}

resource "twingate_resource" "scipi_instance" {
  name              = var.twingate_resource_name
  address           = var.ip_address
  remote_network_id = twingate_remote_network.scipi_network.id
  protocols {
    allow_icmp = true
    tcp {
      policy = "ALLOW_ALL"
    }
    udp {
      policy = "ALLOW_ALL"
    }
  }
}

# TODO create local_exec resource to run docker or docker-compose.yaml with shell script for env vars
