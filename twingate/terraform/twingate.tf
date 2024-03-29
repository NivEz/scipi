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

data "twingate_groups" "access_groups" {
  name = var.twingate_access_group
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

  access {
    group_ids = [for ag in data.twingate_groups.access_groups.groups: ag.id]
  }
}

resource "null_resource" "tokens" {
  provisioner "local-exec" {
    command = "echo ACCESS_TOKEN=${twingate_connector_tokens.scipi_connector_tokens.access_token} >> .env.tokens"
  }

  provisioner "local-exec" {
    command = "echo REFRESH_TOKEN=${twingate_connector_tokens.scipi_connector_tokens.refresh_token} >> .env.tokens"
  }
}
