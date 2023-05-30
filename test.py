from fastapi import  FastAPI, Path
from typing import Optional,List,Literal,Union
from fastapi.routing import APIRouter
from pydantic import BaseModel,Field
from bson import ObjectId
import pymongo
from pymongo import MongoClient 
import requests
import asyncio
import uvicorn
from src.db_func import pets
 # helloooooo




data = [
    {"_id": 1,"name":"roger","animal":"dog","breed":"Husky"},
    {"_id": 2,"name":"gem","animal":"cat","breed":"Tabby"},
    {"_id":3,"name":"tar","animal":"Spider","breed":"Tartula"},
    {"_id":4,"name":"kuttapi","animal":"Fish","breed":"Arownana"},
    {"_id":5,"name":"lucy","animal":"cat","breed":"Siamese"},
    {"_id":6,"name":"sam","animal":"cat","breed":"Siamese"},
    {"_id":7,"name":"tuffy","animal":"dog","breed":"Pomerarian"},
    {"_id":8,"name":"snoopy","animal":"dog","breed":"Dashchund"},
    {"_id":9,"name":"sucky","animal":"Fish","breed":"Sucker Fish"},
]
pets.insert_many(data)
for x in pets.find({}):
    print(x)


app = FastAPI(title="TEST API")

class Pet(BaseModel):
  pet_ID      : int = pets.count_documents({}) + 1
  name    : str = "name"
  animal  : Optional[str] = "animal"
  breed   : str = "breed"

 
@app.get('/')
def index():
    return "WELCOME TO PET DB"

@app.post("/create/")
def create_pet(pet:Pet):
    # if pets.find_one({"pet_ID":ID}) != None:
    # # if _id in pets.find():
    #      return {"Error" :"Data Alreasdy Exists"}
    # else:
        try:
            pet_data = {"pet_ID":pet.pet_ID,"name":pet.name,"animal":pet.animal,"breed":pet.breed}
            pets.insert_one(pet_data)
            return "Done" #insert.inserted_id#pets.find_one({"pet_ID":pet.pet_ID}) 
        except:
            return {"Error":"Error Inserting Data"}
    # pets[_id] = pet
    # return pets

ins = { 
  "_id" : 10,
  "name"  :  "name",
  "animal"  :  "animal",
  "breed"  :  "breed"
  }
# print(create_pet(10,ins))

@app.get('/pet-id/{ID}')  
def get_pet_by_ID(ID:int= Path(description="Serial No. / ID of Pet",gt=0)):
    try:
        return pets.find_one({"_id":ID})
    except:
        return {"Error":"Data Doesnt Exist"}


@app.get('/animals')
def by_animal_Name(animal:Optional[str]):
    if animal == None:
        res = list(pets.find({}))
        return res
    else:
        animal = animal.lower()
        res = list(pets.find({"animal":animal}))
        if len(res) > 0:
            return res
        else: return {'Error':"Data Doesnt Exist"}

print(Pet)
@app.get('/animals')
def by_animalBreed(breed:str):
    res = []
    for _id in pets:
        if pets[_id]["breed"] == breed:
            res.append(pets[_id])
    if len(res) != 0:
        return res
    else: return "Not Found" 



@app.post('/send')
def send(text: str):
    return text

if __name__ == "__main__":
    uvicorn.run(app,port=5001)

