class TaskStatus:
    """
    The parameter status refer to "Not Started", "Doing" and "Completed".
    The status is being taken from the name of the "column/property" in MongoDB.
    """
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
        
    @classmethod
    def from_mongodb_card(cls, card):
        return cls(card["_id"], card["name"], card["status"])