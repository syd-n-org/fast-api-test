from typing import Any, Optional, Dict, List


class dbFunctions:
    @staticmethod
    def read(coll: Any, query: Dict, proj: Dict = {"_id": 0}):
        return coll.find(query, proj)

    @staticmethod
    def read_one(coll: Any, query: Dict, proj: Dict = {"_id": 0}):
        return coll.find_one(query, proj)

    @staticmethod
    def write(coll: Any, insert:List|Dict = None):
        if isinstance(insert,dict):
            return coll.insert_one(insert).acknowledged
        elif isinstance(insert,list):
            return coll.insert_many(insert).acknowledged

    @staticmethod
    def erase_one(coll: Any, key: str, val: str):
        erased = coll.delete_one({key: val})
        return erased.deleted_count

    @staticmethod
    def erase(coll: Any, query: Dict | List = {}):
        erased = coll.delete_many(query)
        return erased.deleted_count

    @staticmethod
    def edit_one(coll: Any, search: Dict = {}, change: Dict = {}):
        upd = coll.update_one(search, {"$set": change})
        return upd

    @staticmethod
    def sort(function: Any, query: List, lmt: None | int = None):
        if lmt:
            return function.sort(query[0], query[1]).limit(lmt)
        else:
            return function.sort(query[0], query[1])

    # @staticmethod
    # def update(coll:Any,insert:List):
