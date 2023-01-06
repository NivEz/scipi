import inquirer
import subprocess
from exceptions import DockerInstallFailed
from choices import CHOICES


def cli():
    choices = [(CHOICES[choice]['display_value'], choice) for choice in CHOICES]
    questions = [
        inquirer.Checkbox(name='installations',
                          message="Choose programs to install",
                          choices=choices,
                          carousel=True,
                          ),
        inquirer.Confirm("begin", message="Begin the installation?", default=True),
    ]
    answers = inquirer.prompt(questions)
    print(answers)
    return
    begin = answers['begin']
    if not begin:
        print("Closing interactive installation...")
        return

    install_docker()

    for package in answers['installations']:
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
