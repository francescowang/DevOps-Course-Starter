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


def get_cards():
    pass

