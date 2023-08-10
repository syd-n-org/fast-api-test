# config.py
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("./local_env.env")
load_dotenv(dotenv_path=dotenv_path)


class Settings:
    proj_name = os.getenv("PROJECT_NAME")
    proj_ver = os.getenv("PROJECT_VERSION")
    db_host = os.getenv("DATABASE_HOST")
    db_port = int(os.getenv("DATABASE_PORT"))
    db_username = ""
    db_pass = ""
    db_auth = os.getenv("DATABASE_AUTH")
    db_name = os.getenv("DATABASE")
    ALL = os.getenv("ALL")


settings = Settings()


class EnvCheck:
    # def __init__(self) -> None:
    db = []

    @staticmethod
    def db_check():
        return f"{settings.db_name}:{type(settings.db_name)} | {settings.db_auth}:{type(settings.db_auth)} | {settings.db_host}:{type(settings.db_host)} | {settings.db_port}:{type(settings.db_port)}"

    @staticmethod
    def proj_check():
        return f"{settings.proj_name} | {settings.proj_ver}"


print(EnvCheck.db_check())
