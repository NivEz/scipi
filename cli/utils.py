import subprocess
import os
import ipaddress
from choices import CHOICES
from exceptions import InvalidIpAddress, IpAddressNotFound, DockerInstallFailed


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
        val = key_val_pairs[key]
        env_string += f"{key_prefix}{key_final}='{val}'\n"

    with open(file_name, "w") as f:
        f.write(env_string)


def install_docker(retry=0, max_retries=1):
    script = './docker-install.sh'
    try:
        shell = subprocess.run(script, cwd="../scripts", shell=True)
        if shell.returncode == 126:
            raise PermissionError
    except PermissionError:
        shell = subprocess.run(f'chmod +x {script} && {script}', cwd="../scripts", shell=True)
    if shell.returncode != 0:
        retry += 1
        if retry != 0 and retry <= max_retries:
            install_docker(retry=retry)
        else:
            raise DockerInstallFailed


def check_if_docker_installed():
    cmd = subprocess.run("docker ps", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return cmd.returncode == 0


def install_package(package):
    if package not in CHOICES:
        return None
    directory = CHOICES[package]['directory']
    script = CHOICES[package]['script']
    try:
        shell = subprocess.run(script, cwd=f"../{directory}")
        if shell.returncode == 126:
            raise PermissionError
    except PermissionError:
        shell = subprocess.run(f'chmod +x {script} && {script}', cwd=f"../{directory}", shell=True)
    if shell.returncode != 0:
        package_short_name = CHOICES[package]['short_name']
        print(f"Could not install {package_short_name}")


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
