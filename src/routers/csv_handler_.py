import pandas as pd
from pprint import pprint
from typing import List
from src.db.connections import all_
from src.db.database_functions import dbFunctions
from src.models.default_models import ResponseModel, RecordModel
from fastapi import APIRouter
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse, FileResponse
from fastapi import APIRouter, status, File, UploadFile, HTTPException


class Handler_csv:
    def __init__(self) -> None:
        self.router = APIRouter()
        self.router.add_api_route(
            path="/csv_upload", endpoint=self.csv_upload, methods=["POST"]
        )
        self.router.add_api_route(
            path="/csv_download_all", endpoint=self.csv_download_all, methods=["GET"]
        )

    async def csv_upload(self, file: UploadFile = File(..., file_name="file.csv")):
        if file.content_type != "text/csv":
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail="Wrong data type",
            )
        else:
            csv = pd.read_csv(file.file, header=0)
            if (
                len([x for x in csv.columns if x not in ["name", "animal", "breed"]])
                > 1
            ):
                raise HTTPException(
                    status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Data Error"
                )
            else:
                csv = csv[["name", "animal", "breed"]]
            start_id = (
                list(
                    dbFunctions.sort(
                        dbFunctions.read(all_, {}, {"pet_id": 1, "_id": 0}),
                        ["pet_id", -1],
                        1,
                    )
                )[0]["pet_id"]+ 1
            )
            csv["pet_id"] = [x for x in range(start_id, csv.shape[0] + start_id)]
            ins = dbFunctions.write(all_, csv.to_dict("records"))
            return HTTPException(
                status_code=status.HTTP_201_CREATED, detail="Data insertedin DB"
            )

    async def csv_download_all(self):
        # pprint(pd.DataFrame(list(test_db.get_collection("dummy").find({},{"_id":0}))))
        query = list(dbFunctions.read(all_, {}))
        df = pd.DataFrame(query)
        iterable = iter([df.to_csv(index=False)])
        return StreamingResponse(
            iterable,
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment;filename=data.csv"},
        )

        # pprint(pd.DataFrame(list(test_db.get_collection("dummy").find({},{"_id":0}))))
        query = list(test_db.get_collection("dummy").find({}, {"_id": 0}))
        df = pd.DataFrame(query)
        iterable = iter([df.to_csv(index=False)])
        return StreamingResponse(
            iterable,
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment;filename=data.csv"},
        )


csv_handler = Handler_csv()
