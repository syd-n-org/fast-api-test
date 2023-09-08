from src.core.config import settings
from src.db.database import Connection

connection = Connection.connect(
    host=settings.db_host,
    port=settings.db_port,
    db=settings.db_name,
    username=settings.db_username,
    password=settings.db_pass,
    auth=settings.db_auth,
all_ = connection[settings.ALL]

