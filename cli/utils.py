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


def build_dot_env_file(key_val_pairs, key_prefix=""):
    env_string = ""
    for key in key_val_pairs:
        env_string += f"{key_prefix}{key.upper()}={key_val_pairs[key]}\n"

    # remove the last line break \n
    env_string = env_string[:-1]

    with open(".env", "w") as f:
        f.write(env_string)
