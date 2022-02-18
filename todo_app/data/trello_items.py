import os
import requests


# global variables
key = os.environ.get("TRELLO_KEY")
token = os.environ.get("TOKEN_KEY")
board = os.environ.get("BOARD_ID")
not_started_id = os.environ.get("NOT_STARTED_ID")
completed_id = os.environ.get("COMPLETED_ID")
doing_id = os.environ.get("DOING_ID")


class Task:
    def __init__(self, id, name, status = "Not Started"):
        self.id = id
        self.name = name
        self.status = status
        
    @classmethod
    def from_trello_card(cls, card, list_name):
        return cls(card["id"], card["name"], list_name)


def get_cards(list_name):
    url_api = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}&cards=open"
    headers = {
        "Accept": "application/json"
    }
    
    response = requests.request(
        "GET",
        url=url_api,
        headers=headers
    )
    
    result = response.json()
    
    tasks = []
    
    for a_list in result: # Not Started, Completed, Doing
        if a_list["name"] == list_name:
            for card in a_list["cards"]:
                task = Task.from_trello_card(card, list_name)
                
                tasks.append(task)
    return tasks


def add_trello_task(title):
    pass

card = get_cards("Not Started")
print(card)