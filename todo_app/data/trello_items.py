import os
import requests


# global variables
key = os.environ.get("TRELLO_KEY")
token = os.environ.get("TOKEN_KEY")
board = os.environ.get("BOARD_ID")
not_started_id = os.environ.get("NOT_STARTED_ID")
completed_id = os.environ.get("COMPLETED_D")
doing_id = os.environ.get("DOING_ID")


class Task:
    def __init__(self, item_id, name, status = "Not Started"):
        self.item_id = item_id
        self.name = name
        self.status = status
        
    @classmethod
    def from_trello_card(cls, card, list_name):
        return cls(card["item_id"], card["name"], list_name)


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
    url_api = f"https://api.trello.com/1/lists/{not_started_id}/cards?name={title}&key={key}&token={token}"

    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "POST",
    url=url_api,
    headers=headers
    )
    
def delete_trello_task(item_id):

    call = f"https://api.trello.com/1/cards/{item_id}?key={key}&token={token}"

    headers = {
    "Accept": "application/json"
    }

    return requests.request("DELETE", url=call, headers=headers)


def completed_trello_task(item_id):

    url_api = f"https://api.trello.com/1/cards/{item_id}?item_idList={completed_id}&key={key}&token={token}"

    headers = {
    "Accept": "application/json"
    }
    
    return requests.request("PUT", url=url_api, headers=headers)


def doing_trello_task(item_id):

    url_api = f"https://api.trello.com/1/cards/{item_id}?item_idList={doing_id}&key={key}&token={token}"

    headers = {
    "Accept": "application/json"
    }

    return requests.request("PUT", url=url_api, headers=headers)


def unfinished_trello_task(item_id):

    url_api = f"https://api.trello.com/1/cards/{item_id}?item_idList={doing_id}&key={key}&token={token}"

    headers = {
    "Accept": "application/json"
    }

    return requests.request("PUT", url=url_api, headers=headers)