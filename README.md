# SciPi

Interactive CLI that helps you set up your Raspberry Pi

---

## About
SciPi (pronounced "saipai") is an interactive CLI tool based on Python that will let you setup your Raspberry Pi quite fast and easily.
<br>
SciPi is used for Raspberry Pi home labs, and it uses Docker, docker compose and even Terraform.

Disclaimer:
<br>
This is a personal project, and it has nothing to do with SciPy.

---

### For now, SciPi supports the following installations and setups:

✅ Docker
<br>
✅ Portainer
<br>
✅ Twingate (zero trust network)
<br>
✅ Pi-hole

---

## Getting started

Login to your Raspberry Pi via SSH:
```
ssh <USER>@<IP>
```

Clone the project:
```
git clone https://github.com/NivEz/scipi.git
```

cd into the project:
```
cd scipi
```

Set up SciPi (python venv and requirements installation):
```
./scripts/setup.sh
```

You might need execution permissions to execute the setup script:
```
chmod +x ./scripts/setup.sh
```

Execute the python interactive CLI:
```
./scripts/scipi.sh
```
