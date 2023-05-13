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

variable "twingate_access_group" {
  type = string
  default = "Everyone"
  description = "The name of the group to grant access to the twingate scipi instance"
}
