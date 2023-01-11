import inquirer
import subprocess
from exceptions import DockerInstallFailed
from choices import CHOICES
from utils import get_ip, build_dot_env_file


def cli():
    choices = [(CHOICES[choice]['display_value'], choice) for choice in CHOICES]
    installation_questions = [
        inquirer.Checkbox(name='packages',
                          message="Choose programs to install",
                          choices=choices,
                          carousel=True,
                          )
    ]
    answers = inquirer.prompt(installation_questions)
    print(answers)

    if 'twingate' in answers['packages']:
        twingate_key_vals = inquirer.prompt([
            inquirer.Text("network", message="What is your Twingate network? (e.g john for john.twingate.com)", validate=lambda _,x: x != ""),
            inquirer.Password("api_token", message="Insert Twingate API token", validate=lambda _,x: x != ""),
            inquirer.Text("remote_network", message="Choose remote network name", default="SciPi network"),
            inquirer.Text("resource_name", message="Choose resource name", default="internal"),
        ])

        # TODO it might be better to export the vars, consider it
        build_dot_env_file(twingate_key_vals, key_prefix="TF_VAR_")

    ip = get_ip()
    begin_questions = [inquirer.Confirm("begin", message=f"Begin the installation on IP {ip}?", default=True)]
    begin_answer = inquirer.prompt(begin_questions)

    if not begin_answer['begin']:
        print("Closing interactive installation...")
        return

    return

    install_docker()

    for package in answers['packages']:
        print("\n-----\n")
        install_package(package)
        if 'creds' in CHOICES[package]:
            # TODO - Ask for tokens as password inputs
            pass


def install_docker():
    shell = subprocess.run('./docker-install.sh', cwd="../scripts")
    if shell.returncode != 0:
        raise DockerInstallFailed


def install_package(package):
    directory = CHOICES[package]['directory']
    try:
        shell = subprocess.run('./install.sh', cwd=f"../{directory}")
        print(shell.returncode)
    except PermissionError:
        shell = subprocess.run('chmod +x ./install.sh && ./install.sh', cwd=f"../{directory}", shell=True)
    if shell.returncode != 0:
        package_short_name = CHOICES[package]['short_name']
        print(f"Could not install {package_short_name}")


if __name__ == '__main__':
    cli()
