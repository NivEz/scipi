variable "twingate_network" {
  type = string
}

variable "twingate_api_token" {
  type = string
}

variable "twingate_remote_network" {
  type = string
  default = "SciPi network"
}

variable "twingate_resource_name" {
  type = string
  default = "internal"
}

variable "ip_address" {
  type = string
}
