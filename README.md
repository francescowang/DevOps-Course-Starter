# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Steps

**Module 1**

 - [ ] Clone the repository
 - [ ] Delete .git file or run ```git remote remove origin``` to unlink from the original project
 - [ ] Initialise a new repository if you deleted the .git file
 - [ ] If your default shell is zsh, change it to bash
 - [ ] Run these commands

```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```

```poetry install```

```cp .env.template .env```

 - [ ] In the .env file, add a secret key
```
# this prints out a random key, copy and paste it to your SECRET_KEY variable
import os
os.urandom(16)
```
 - [ ] In your settings.json file, add the following code snippet
```
{
		"python.terminal.activateEnvironment":  true,
		"python.terminal.activateEnvInCurrentTerminal":  true,
		"python.defaultInterpreterPath":  "./.venv/bin/python",
		"python.formatting.blackPath":  "black",
		"editor.tabCompletion":  "on",
		"workbench.colorCustomizations": {
				"terminal.foreground"  :  "#10d52b",
				"terminal.background"  :  "#000000",
		},
		"python.formatting.provider":  "black",
		"python.linting.enabled":  true,
}
```

**Module 2**

```poetry add requests```

In the .env file, add the trello API keys and IDs. Login to Trello and use Postman to get started. E.g.
```
SECRET_KEY=
TRELLO_KEY=
TRELLO_TOKEN=
BOARD_ID=
NOT_STARTED_ID=
DOING_ID=
COMPLETED_ID=
```

**Module 3**
Install pytest module ```poetry add pytest```
Create a .env.test file ```touch .env.test```
Copy from the .env.template and provide "fake" details for testing purposes

**Testing the App**

Run the following command from the parent directory:

```poetry run pytest```

If you wish to run only selected tests:

```poetry run pytest todo_app/tests/<file that needs testing>```

Or cd into the directory:

```cd todo_app/tests```
```poetry run run pytest/<file that needs testing>```


**Module 4**

- [ ] Install ansible using homebrew

```
brew install ansible
```

https://formulae.brew.sh/formula/ansible

or

- [ ] Install ansible using pip in your .venv
```
pip install ansible
```

Run ```ansible --version``` to check if the installation succeeded
You are now going to SSH from the Control Node into the Managed Node

Note:
- controller-ip-address is the Control Node 
- host-ip-address is the Managed Node

```
ssh ec2-user@<controller-ip-address>
```

- [ ] Once logged in the Control Node, create an SSH key pair with this command
```
ssh-keygen
```
- [ ] Now enter the password one last time
```
ssh-copy-id ec2-user@<controller-ip-address>
```

- You are now logged in Control Node using SSH
- You can end an SSH session with the command ```exit```

Repeat the process for Managed Node by running the following commands and enter the password

- [ ] ```ssh ec2-user@<host-ip-address>```
- [ ] ```ssh-keygen```
- [ ] ```ssh-copy-id ec2-user@<host-ip-address>```

Go back to the project directory, you can now ssh into both nodes without the password
Get into Controlled Node, then Managed Node and see the authorised keys

```
cat ~/.ssh/authorized_keys
```

- [ ] Install this extension -> Remote - SSH 
- [ ] Command + shift N to open a new window
- [ ] Click on the purple rectable bottom left and click on connect host
- [ ] Enter the ec2-user@<controller-ip-address>
- [ ] Create/Edit an inventory.ini file and playbook.yml file

- [ ] Run the following commands:
```
ansible -i inventory.ini
```
```
ansible franky-host -i inventory.ini -m ping
```
Run ```whoami``` to find out username of the current user when this command is invoked

```
ansible-playbook playbook.yml -i inventory.ini
```

**Module 5**

```
poetry add gunicorn
```

```
# building an image for development
# it automatically adds colon and 'latest' if you just leave the name e.g. todoapp
docker build --tag todoapp:dev . --target development
# this is the command for the development in your localhost
docker run --env-file .env -p 5001:5000 --volume $(pwd)/todo_app:/opt/todo_app todoapp:dev



docker build --tag todoapp:prod . --target production
# port 5000 is taken by airplay
#running a container based on the todoapp:prod image
docker run --env-file .env -it -p 5001:8000 todoapp:prod




# for debugging
<!-- docker run --entrypoint bash -it todoapp:dev -->
<!-- docker run -it todoapp:prod -->
```