from app.db.db import MongoManager

db = MongoManager()


async def get_database() -> MongoManager:
    return db
