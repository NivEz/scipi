terraform {
  required_providers {
    twingate = {
      source = "twingate/twingate"
    }
  }
}

provider "twingate" {
  api_token = "" // get from vars
  network   = "" // get from vars
}

resource "twingate_remote_network" "scipi_network" {
  name = "SciPi network"
}

resource "twingate_connector" "scipi_connector" {
  remote_network_id = twingate_remote_network.scipi_network.id
}

resource "twingate_connector_tokens" "scipi_connector_tokens" {
  connector_id = twingate_connector.scipi_connector.id
}

resource "twingate_resource" "scipi_instance" {
  name              = "SciPi"
  address           = "" // get from vars
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
