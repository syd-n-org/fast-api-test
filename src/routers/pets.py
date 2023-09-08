from src.db.connections import all_
from src.models.default_models import ResponseModel, RecordModel
from src.db.database_functions import dbFunctions
from fastapi import APIRouter


class AllPets:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            path="/all-records",
            endpoint=self.all_record,
            methods=["GET"],
            response_model=ResponseModel,
        )
        self.router.add_api_route(
            path="/add-records",
            endpoint=self.add_record,
            methods=["POST"],
            response_model=ResponseModel,
        )
        self.router.add_api_route(
            path="/edit-records",
            endpoint=self.edit_record,
            methods=["PUT"],
            response_model=ResponseModel,
        )
        self.router.add_api_route(
            path="/purge-records",
            endpoint=self.purge_record,
            methods=["DELETE"],
            response_model=ResponseModel,
        )

    @staticmethod
    async def all_record():
        data = dbFunctions.read(all_, {})
        print(data)
        return ResponseModel(content=list(data))

    @staticmethod
    async def add_record(add_record_query: RecordModel):
        data = add_record_query.dict()
        if not dbFunctions.read_one(all_, {"pet_id": data["pet_id"]}):
            # ins = dbFunctions.write_one(all_,data)
            return ResponseModel(
                content=str(dbFunctions.write(all_, data)),
                message="Data Inserted",
            )
        else:
            return ResponseModel(response_code=401, message="Data Already Exists")

    @staticmethod
    async def edit_record(edit_record_query: RecordModel):
        data = edit_record_query.dict()
        search = {"pet_id": data["pet_id"]}
        if dbFunctions.read_one(all_, search):
            updt = dbFunctions.edit_one(all_, search, data)
            return ResponseModel(content=updt.raw_result, message="Data Edited")
        else:
            return ResponseModel(response_code=404, message="Data Does Not Exist")

    @staticmethod
    async def purge_record():
        purged = dbFunctions.erase(all_, {})
        return ResponseModel(content=purged, message="All Records Deleted")


allpets = AllPets()
