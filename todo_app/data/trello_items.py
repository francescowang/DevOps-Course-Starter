import os
import requests


# global variables
key = os.environ.get("TRELLO_KEY")
token = os.environ.get("TOKEN_KEY")
board = os.environ.get("BOARD_ID")
not_started_id = os.environ.get("NOT_STARTED_ID")
doing_id = os.environ.get("DOING_ID")
completed_id = os.environ.get("COMPLETED_ID")


class Task:
    def __init__(self, id, name, status="Not Started"):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list_name):
        return cls(card["id"], card["name"], list_name)


def get_cards(list_name):
    url_api = f"https://api.trello.com/1/boards/{board}/lists?key={key}&token={token}&cards=open"
    headers = {"Accept": "application/json"}

    response = requests.request("GET", url=url_api, headers=headers)

    result = response.json()

    tasks = []

    for a_list in result:  # a_lists refer to NOT STARTED, DOING, COMPLETED lists in trello board
        if a_list["name"] == list_name:
            for card in a_list["cards"]:
                task = Task.from_trello_card(card, list_name)

                tasks.append(task)
    return tasks


# Add
def add_trello_task(title):
    url_api = f"https://api.trello.com/1/lists/{not_started_id}/cards?name={title}&key={key}&token={token}"

    headers = {"Accept": "application/json"}

    response = requests.request("POST", url=url_api, headers=headers)


# Delete
def delete_trello_task(delete_task):

    url_api = f"https://api.trello.com/1/cards/{delete_task}?key={key}&token={token}"

    headers = {"Accept": "application/json"}

    return requests.request("DELETE", url=url_api, headers=headers)


# Not Started
def not_started_trello_task(id):

    url_api = f"https://api.trello.com/1/cards/{id}?idList={doing_id}&key={key}&token={token}"

    headers = {"Accept": "application/json"}

    return requests.request("PUT", url=url_api, headers=headers)


# Doing
def doing_trello_task(doing_task):

    url_api = f"https://api.trello.com/1/cards/{doing_task}?idList={doing_id}&key={key}&token={token}"
    print(url_api)

    headers = {"Accept": "application/json"}

    return requests.request("PUT", url=url_api, headers=headers)


# Completed
def completed_trello_task(id):

    url_api = f"https://api.trello.com/1/cards/{id}?idList={completed_id}&key={key}&token={token}"

    headers = {"Accept": "application/json"}

    return requests.request("PUT", url=url_api, headers=headers)