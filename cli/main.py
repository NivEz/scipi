import inquirer
import subprocess
from exceptions import DockerInstallFailed
from choices import CHOICES
from utils import get_ip, build_env_vars_file, open_text_editor


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
            inquirer.Text("network", message="What is your Twingate network? (e.g john for john.twingate.com)",
                          validate=lambda _, x: x != ""),
            inquirer.Text("remote_network", message="Choose remote network name", default="SciPi network"),
            inquirer.Text("resource_name", message="Choose resource name", default="internal"),
            inquirer.Text("api_token", message="In the next step paste your api token in the text editor", default=""),
        ])

        api_token = open_text_editor(file_path="api_token.txt")
        twingate_key_vals['api_token'] = api_token

        print("------------------------")
        print(twingate_key_vals)

        # TODO it might be better to export the vars, consider it
        build_env_vars_file(twingate_key_vals, key_prefix="TF_VAR_", file_name=".env.tf_vars")

    ip = get_ip()
    begin_questions = [inquirer.Confirm("begin", message=f"Begin the installation on IP {ip}?", default=True)]
    begin_answer = inquirer.prompt(begin_questions)

    if not begin_answer['begin']:
        print("Closing interactive installation...")
        return

    install_docker()

    for package in answers['packages']:
        print("\n-----\n")
        install_package(package)


def install_docker():
    script = './docker-install.sh'
    try:
        shell = subprocess.run(script, cwd="../scripts", shell=True)
        print(shell.returncode, "RETURNNNNNNN")
        if shell.returncode == 126:
            raise PermissionError
    except PermissionError:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        shell = subprocess.run(f'chmod +x {script} && {script}', cwd="../scripts", shell=True)
    if shell.returncode != 0:
        raise DockerInstallFailed


def install_package(package):
    directory = CHOICES[package]['directory']
    script = CHOICES[package]['script']
    try:
        shell = subprocess.run(script, cwd=f"../{directory}")
        print(shell.returncode, "RETURNNNNNNN")
        if shell.returncode == 126:
            raise PermissionError
    except PermissionError:
        shell = subprocess.run(f'chmod +x {script} && {script}', cwd=f"../{directory}", shell=True)
    if shell.returncode != 0:
        package_short_name = CHOICES[package]['short_name']
        print(f"Could not install {package_short_name}")


if __name__ == '__main__':
    cli()
