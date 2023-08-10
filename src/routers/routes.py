from src.routers.pets import allpets
from src.routers.csv_handler_ import csv_handler


class ApiRoutes:
    def __init__(self, app):
        app.include_router(allpets.router, prefix="/api/v1/all-pets", tags=["All Pets"])
        app.include_router(
            csv_handler.router, prefix="/api/v1/csv-handler", tags=["Media"]
        )
