import os
import pymongo
from todo_app.data.item_status import TaskStatus
from bson import ObjectId



class MongoDB_Items:
    def __init__(self):
        connection_string = os.environ.get("CONNECTION_STRING")
        mongodb = os.environ.get("MONGO_DB")
        client = pymongo.MongoClient(connection_string)
        db = client[mongodb]
        self.collection = db.todo_collection
    
    def get_mongo_cards(self):
        return [TaskStatus.from_mongodb_card(card) for card in self.collection.find()]
    
    def add_mongo_card(self, title):
        self.collection.insert_one({
            "name": title,
            "status": "NOT STARTED"
        })
    
    def delete_mongo_card(self, id):
        
        queries = { 
                "_id": ObjectId(id)
        }
        print(type(queries))
        self.collection.delete_one(queries)
    
    def not_started_mongo_card(self, id):
        
        query = {
            "_id": ObjectId(id)
        }
        new_query = {
            "$set": {"status": "NOT STARTED"}
            
        }
        self.collection.update_one(query, new_query)
    
    def doing_mongo_card(self, id):
        
        query = {
            "_id": ObjectId(id)
        }
        new_query = {
            "$set": {"status": "DOING"}
            
        }
        self.collection.update_one(query, new_query)
    
    def completed_mongo_card(self, id):
        
        query = {
            "_id": ObjectId(id)
        }
        new_query = {
            "$set": {"status": "COMPLETED"}
            
        }
        self.collection.update_one(query, new_query)