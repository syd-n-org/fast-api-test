from fastapi import FastAPI
# from routers.csv_handler_ import csv_handler
from src.core.config import settings,EnvCheck
from src.routers.routes import ApiRoutes


app = FastAPI(title=settings.proj_name,version=settings.proj_ver)
ApiRoutes(app)

