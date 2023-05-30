from fastapi import  FastAPI, Path, APIRouter
from typing import Optional,List,Literal,Union
from fastapi.routing import APIRouter
from pydantic import BaseModel,Field
from bson import ObjectId
import pymongo
from pymongo import MongoClient 
import requests
import asyncio
import uvicorn
from src.db_func.db import pets
 # helloooooo




# data = [
#     {"_id": 1,"name":"roger","animal":"dog","breed":"Husky"},
#     {"_id": 2,"name":"gem","animal":"cat","breed":"Tabby"},
#     {"_id":3,"name":"tar","animal":"Spider","breed":"Tartula"},
#     {"_id":4,"name":"kuttapi","animal":"Fish","breed":"Arownana"},
#     {"_id":5,"name":"lucy","animal":"cat","breed":"Siamese"},
#     {"_id":6,"name":"sam","animal":"cat","breed":"Siamese"},
#     {"_id":7,"name":"tuffy","animal":"dog","breed":"Pomerarian"},
#     {"_id":8,"name":"snoopy","animal":"dog","breed":"Dashchund"},
#     {"_id":9,"name":"sucky","animal":"Fish","breed":"Sucker Fish"},
# ]

# pets.insert_many(data)


# for x in pets.find({}):
#     print(x)

app = FastAPI(title="TEST API")

class Pet(BaseModel):
  pet_ID  : int 
  name    : str 
  animal  : str 
  breed   : str 

class HomepageMsgs(BaseModel):
    create : str = "/create/"
    byID : str = ""

class PetDB():
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(path='/home',endpoint=self.index,
                                  methods=["GET"],summary="Landing Page")
        self.router.add_api_route(path='/animals/{animals}',endpoint=self.show_animals,methods=["GET"],
                                  summary="Show all records")
        self.router.add_api_route(path='/create/',endpoint=self.create_pet,
                                  methods=["POST"],response_model=Pet,summary="Create Pet in DB")
        self.router.add_api_route(path='find-byID',endpoint=self.get_pet_by_ID,
                                  methods=["GET"],summary="Find pet by ID")

        
    async def index(self):
        welcome_text = f"WELCOME TO PET DB: \nFind Pet by ID @ http://127.0.0.1:5008/create/"
        return welcome_text
    
    async def create_pet(self,pet:Pet):
        pet_data = pet.dict() #{"pet_ID":pet.pet_ID,"name":pet.name,"animal":pet.animal,"breed":pet.breed}
        try:
            pets.insert_one(pet_data)
            return "Done" #insert.inserted_id#pets.find_one({"pet_ID":pet.pet_ID}) 
        except:
            return {"Error":"Error Inserting Data"}
        
    async def get_pet_by_ID(self,ID:int,gt=0):
        try:
            return pets.find_one({"_id":ID})
        except:
            return {"Error":"Data Doesnt Exist"}
        
    async def show_animals(self,animal:Optional[str]= None):
        if animal == None:
            res = list(pets.find({}))
            return res
        else:
            animal = animal.lower()
            res = list(pets.find({"animal":animal}))
            if len(res) > 0:
                return res
            else: return {'Error':"Data Doesnt Exist"}
                                          
petdb = PetDB()
app.include_router(petdb.router,tags=["all"])
# if __name__ == "__main__":
#     uvicorn.run(app,port=5001)

