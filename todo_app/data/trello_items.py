import os
import requests

class TaskStatus:
    """
    The parameter status refer to "Not Started", "Doing" and "Completed".
    The status is being taken from the name of the "list" in Trello, 
    so it will be whatever column the card belongs to on your Trello board.
    """
    def __init__(self, id, name, status): # e.g. status="Not Started"
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list_name):
        return cls(card["id"], card["name"], list_name)


class TrelloItems:
    def __init__(self):
        self.key = os.environ.get("TRELLO_KEY")
        self.token = os.environ.get("TRELLO_TOKEN")
        self.board = os.environ.get("BOARD_ID")
        self.not_started_id = os.environ.get("NOT_STARTED_ID")
        self.doing_id = os.environ.get("DOING_ID")
        self.completed_id = os.environ.get("COMPLETED_ID")


    def get_cards(self):
        url_api = f"https://api.trello.com/1/boards/{self.board}/lists?key={self.key}&token={self.token}&cards=open"
        headers = {"Accept": "application/json"}

        response = requests.request("GET", url=url_api, headers=headers)

        result = response.json()

        tasks = []

        for a_list in result:  # a_lists refer to NOT STARTED, DOING, COMPLETED lists in trello board
            for card in a_list["cards"]:
                task = TaskStatus.from_trello_card(card, a_list["name"]) # calling all lists -> a_list["name"]
                tasks.append(task)
        return tasks

    # Add
    def add_trello_task(self, title):
        url_api = f"https://api.trello.com/1/lists/{self.not_started_id}/cards?name={title}&key={self.key}&token={self.token}"

        headers = {"Accept": "application/json"}

        response = requests.request("POST", url=url_api, headers=headers)


    # Delete
    def delete_trello_task(self, delete_task):

        url_api = f"https://api.trello.com/1/cards/{delete_task}?key={self.key}&token={self.token}"

        headers = {"Accept": "application/json"}

        return requests.request("DELETE", url=url_api, headers=headers)


    # Not Started
    def not_started_trello_task(self, not_started_task):

        url_api = f"https://api.trello.com/1/cards/{not_started_task}?idList={self.not_started_id}&key={self.key}&token={self.token}"

        headers = {"Accept": "application/json"}

        return requests.request("PUT", url=url_api, headers=headers)


    # Doing
    def doing_trello_task(self, doing_task):

        url_api = f"https://api.trello.com/1/cards/{doing_task}?idList={self.doing_id}&key={self.key}&token={self.token}"
        print(url_api)

        headers = {"Accept": "application/json"}

        return requests.request("PUT", url=url_api, headers=headers)


    # Completed
    def completed_trello_task(self, completed_task):

        url_api = f"https://api.trello.com/1/cards/{completed_task}?idList={self.completed_id}&key={self.key}&token={self.token}"

        headers = {"Accept": "application/json"}

        return requests.request("PUT", url=url_api, headers=headers)