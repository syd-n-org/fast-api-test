import pymongo
from pymongo import MongoClient

client = MongoClient("localhost:27017")
fn_db = client.footnotes
test_db = client.test
pets = test_db.pets

def distinct(key="", query={}, col=""):
        return fn_db[col].distinct(key,query)

def find_one(query,col):
    return fn_db.get_collection(col).find_one(query,sort=[("_id",pymongo.DESCENDING)])

def find_all(query, col):
    return list(fn_db.get_collection(col).find(query, sort=[("_id", pymongo.DESCENDING)]))
