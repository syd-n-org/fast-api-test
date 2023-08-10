from src.core.config import EnvCheck
from src.db.database import db
coll = db["ANIMALS_ALL"]
print(EnvCheck.db_check())
print(EnvCheck.proj_check())
print(coll.find_one({"pet_id": 0},{"_id":0}))
