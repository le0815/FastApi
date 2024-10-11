from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from models import model
from config.database import engine, Sessionlocal
from sqlalchemy.orm import Session

app = FastAPI()

model.Base.metadata.create_all(bind = engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db

    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/me")
async def get_me():
    return {"Msg": "test"}

class Test(BaseModel):
    name : str
    age  : int | None = None

@app.post("/submit")
async def submit(item: Test):
    print(item)
    return item

@app.get("/items")
async def printItem(*, channelId: int, accountId: int | None = None, db: db_dependency):
    post = db.query(model.Channel).filter(model.Channel.id == channelId).first()

    return post

@app.put("/items/{item_name}")
async def CreateItem(item_name: str, item: Test):
    return {"name": item_name, **item.model_dump()}
