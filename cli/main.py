import inquirer
from utils import *


def cli():
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
            inquirer.Text("twingate_remote_network", message="Choose remote network name", default="SciPi network"),
            inquirer.Text("twingate_resource_name", message="Choose resource name", default="internal"),
            inquirer.Text("twingate_access_group", message="Twingate group name to grant access to the scipi resource", default="Everyone"),
            inquirer.Text("twingate_api_token", message="In the next step paste your api token in the text editor", default=""),
        ])

        api_token = open_text_editor(file_path="api_token.txt")
        twingate_key_vals['twingate_api_token'] = api_token

        env_variables = twingate_key_vals

    ip = get_ip()
    env_variables["ip_address"] = ip
    build_env_vars_file(env_variables, key_prefix="TF_VAR_", file_name=".env.tf_vars")

    begin_questions = [inquirer.Confirm("begin", message=f"Begin the installation on IP {ip}?", default=True)]
    begin_answer = inquirer.prompt(begin_questions)

    if not begin_answer['begin']:
        print("Closing interactive installation...")
        return

    install_docker()

    for package in answers['packages']:
        print("\n----------\n")
        install_package(package)


if __name__ == '__main__':
    cli()
