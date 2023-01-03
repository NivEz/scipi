import inquirer
import subprocess
from exceptions import DockerInstallFailed

CHOICES_DICT = {
    'portainer': {
        'display_value': 'Portainer',
        'short_name': 'Portainer',
        'directory': 'portainer',
    },
    'pihole': {
        'display_value': 'Pi-hole',
        'short_name': 'Pi-hole',
        'directory': 'pi-hole',
    },
    'twingate': {
        'display_value': 'Twingate (Zero Trust)',
        'short_name': 'Twingate',
        'directory': 'terraform',
        'creds': {},
    },
    'shut_down_container': {
        'display_value': 'Remote shut down container',
        'short_name': 'Shut down container',
        'directory': 'manager',
    },
    'monitoring': {
        'display_value': 'Monitoring tools (Prometheus + Grafana)',
        'short_name': 'Monitoring tools',
        'directory': 'monitoring',
    }
}


def cli():
    choices = [(CHOICES_DICT[choice]['display_value'], choice) for choice in CHOICES_DICT]
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
        if 'creds' in CHOICES_DICT[package]:
            # TODO - Ask for tokens as password inputs
            pass


def install_docker():
    shell = subprocess.run('./docker-install.sh', cwd="../scripts")
    if shell.returncode != 0:
        raise DockerInstallFailed


def install_package(package):
    directory = CHOICES_DICT[package]['directory']
    try:
        shell = subprocess.run('./install.sh', cwd=f"../{directory}")
        print(shell.returncode)
    except PermissionError:
        shell = subprocess.run('chmod +x ./install.sh && ./install.sh', cwd=f"../{directory}", shell=True)
    if shell.returncode != 0:
        package_short_name = CHOICES_DICT[package]['short_name']
        print(f"Could not install {package_short_name}")


if __name__ == '__main__':
    cli()
