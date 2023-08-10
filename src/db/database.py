from pymongo import MongoClient
from src.core.config import settings


class Connection:
    def __init__(self):
        pass

    @classmethod
    def connect(self, host, port, db, username, password, auth):
        client = MongoClient(
            host=host, port=port, username=username, password=password, authSource=auth
        )
        db = client[db]
        return db


# def distinct(key="", query={}, col=""):
#         return fn_db[col].distinct(key,query)
# def find_one(query,col):
#     return fn_db.get_collection(col).find_one(query,sort=[("_id",pymongo.DESCENDING)])
# def find_all(query, col):
#     return list(fn_db.get_collection(col).find(query, sort=[("_id", pymongo.DESCENDING)]))
# print(list(db.get_collection("PETS").find({})))
