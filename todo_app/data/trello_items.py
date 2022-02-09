import os
import requests


# global variables
key = os.environ.get("FRANKY_KEY")
token = os.environ.get("FRANKY_TOKEN")
board = os.environ.get("BOARD_ID")
unfinished_id = os.environ.get("UNFINISHED_ID")
completed_id = os.environ.get("COMPLETED_ID")
doing_id = os.environ.get("DOING_ID")


class Task:
    def __init__(self, id, name, status = "Unfinished"):
        self.id = id
        self.name = name
        self.status = status
        
    @classmethod
    def from_trello_card(cls, card, list_name):
        return cls(card["id"], card["name"], list_name)

