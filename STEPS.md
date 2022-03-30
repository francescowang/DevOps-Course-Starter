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
TOKEN_KEY=
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

