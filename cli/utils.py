import subprocess
import os
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


def open_text_editor(text_editor="nano", file_path="", default_text="", cursor_line=0, delete_when_finish=True):
    if not file_path:
        raise ValueError("file_path argument is required")
    if cursor_line > 0:
        command = f"{text_editor} +{cursor_line} {file_path}"
    else:
        command = f"{text_editor} {file_path}"
    if default_text:
        with open(file_path, "w") as f:
            f.write(default_text)
    subprocess.run(command, shell=True)
    with open(file_path) as f:
        text = f.read().strip()

    if delete_when_finish:
        os.remove(file_path)

    return text
