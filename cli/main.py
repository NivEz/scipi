import inquirer
from utils import *
import tzlocal


def docker_cli():
    is_docker_installed = check_if_docker_installed()
    if is_docker_installed:
        return True
    print("In the following step docker will be installed.\n"
          "After the installation finishes logout and log \n"
          "back into your RPI in order to continue with the \n"
          "installation of the other packages.")
    question = inquirer.prompt([
        inquirer.Confirm("install_docker",
                         message=f"Are you ready to proceed?",
                         default=True)
    ])
    if not question['install_docker']:
        print("Closing interactive installation...")
        return False

    install_docker()


def cli():
    is_docker_ready = docker_cli()
    if not is_docker_ready:
        print("\nIt appears that Docker was not installed or configured properly on your RPI.")
        print("Maybe it is and you just forgot to logout from the shell?")
        return

    choices = [(CHOICES[choice]['display_value'], choice) for choice in CHOICES]
    choices.insert(0, "Docker")
    installation_questions = [
        inquirer.Checkbox(name='packages',
                          message="Choose programs to install",
                          choices=choices,
                          carousel=True,
                          locked=["Docker"]
                          )
    ]
    answers = inquirer.prompt(installation_questions)

    env_variables = {}

    if 'twingate' in answers['packages']:
        twingate_key_vals = inquirer.prompt([
            inquirer.Text("twingate_network", message="What is your Twingate network? (e.g john for john.twingate.com)",
                          validate=lambda _, x: x != ""),
            inquirer.Text("twingate_remote_network", message="Choose remote network name", default="SciPi"),
            inquirer.Text("twingate_resource_name", message="Choose resource name", default="internal"),
            inquirer.Text("twingate_access_group", message="Twingate group name to grant access to the scipi resource",
                          default="Everyone"),
            inquirer.Text("twingate_api_token", message="In the next step paste your api token in the text editor",
                          default=""),
        ])

        api_token = open_text_editor(file_path="api_token.txt")
        twingate_key_vals['twingate_api_token'] = api_token

        env_variables = twingate_key_vals

    if 'pihole' in answers['packages']:
        pihole_env = {'timezone': tzlocal.get_localzone_name()}
        build_env_vars_file(pihole_env, file_name=".env.pihole", upper=True)

    ip = get_ip()
    env_variables["ip_address"] = ip
    # adjusting the env file to Terraform
    build_env_vars_file(env_variables, key_prefix="TF_VAR_", file_name=".env.tf_vars")

    begin_questions = [inquirer.Confirm("begin", message=f"Begin the installation on IP {ip}?", default=True)]
    begin_answer = inquirer.prompt(begin_questions)

    if not begin_answer['begin']:
        print("Closing interactive installation...")
        return

    for package in answers['packages']:
        if package not in CHOICES:
            continue
        print("\n----------")
        print(f"Installing ${CHOICES[package]['short_name']}...")
        print("----------\n")
        install_package(package)


if __name__ == '__main__':
    cli()
