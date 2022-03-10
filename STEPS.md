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

