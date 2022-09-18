from fastapi import FastAPI
from app.api.api import router
from app.db import db
app = FastAPI()

API_URL = "mongodb://localhost:27017/"
@app.on_event("startup")
async def startup():
    await db.connect_to_database(path=API_URL)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()

app.include_router(router)
