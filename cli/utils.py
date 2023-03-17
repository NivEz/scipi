import subprocess
import ipaddress
from exceptions import InvalidIpAddress, IpAddressNotFound


def get_ip():
    shell = subprocess.run("hostname -I | awk '{print $1}'", shell=True, capture_output=True, text=True)
    if shell.returncode != 0:
        raise IpAddressNotFound
    ip = shell.stdout.replace("\n", "")
    validate_ip_address(ip)
    return ip


def validate_ip_address(ip_string):
    try:
        ipaddress.ip_address(ip_string)
    except ValueError:
        raise InvalidIpAddress(ip_string)


def build_env_vars_file(key_val_pairs, key_prefix="", file_name=".env", upper=False):
    env_string = ""
    for key in key_val_pairs:
        key_final = key.upper() if upper else key
        env_string += f"{key_prefix}{key_final}={key_val_pairs[key]}\n"

    with open(file_name, "w") as f:
        f.write(env_string)
