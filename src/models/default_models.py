from pydantic import BaseModel
from typing import Any, Optional
# from src.db.connections import db

class ResponseModel(BaseModel):
    content: Any
    response_code: int = 200
    message: Optional[str]

class RecordModel(BaseModel):
    pet_id  : int #= list(db.get_collection("ANIMAL_ALL").find({}).sort(key_or_list="pet_id",direction=-1))[0]
    name    : str
    animal  : str
    breed   : str