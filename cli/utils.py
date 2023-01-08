import subprocess
import ipaddress
from exceptions import InvalidIpAddress


def get_ip():
    shell = subprocess.run("hostname -I | awk '{print $1}'")
    ip = shell.stdout
    validate_ip_address(ip)
    return ip


def validate_ip_address(ip_string):
    try:
        ipaddress.ip_address(ip_string)
    except ValueError:
        raise InvalidIpAddress(ip_string)

