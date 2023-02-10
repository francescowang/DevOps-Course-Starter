import os
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id):
        self.user_id = user_id

    def get_id(self):
        return self.user_id
    

    
    @property
    def role(self):
        print(self.user_id)
        print(os.environ.get("ADMIN_ID"))
        if self.user_id == os.environ.get("ADMIN_ID"):
            return "admin"
        elif self.user_id == os.environ.get("WRITER_ID"):
            return "writer"
        else:
            return "reader"