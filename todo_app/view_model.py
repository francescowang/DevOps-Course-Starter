from typing import List
from todo_app.data.trello_items import TaskStatus


class TaskViewModel:
    def __init__(self, items: List[TaskStatus]) -> None:
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def not_started_items(self):
        return [item for item in self._items if item.status == "Not Started"]

    @property
    def doing_items(self):
        return [item for item in self._items if item.status == "Doing"]

    @property
    def completed_items(self):
        return [item for item in self._items if item.status == "Completed"]