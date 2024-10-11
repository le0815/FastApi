from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
import model
import schema
from config.database import engine, Sessionlocal
from sqlalchemy.orm import Session

from schema import Message

app = FastAPI()

model.Base.metadata.create_all(bind = engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db

    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@app.put("/pushmsg/", response_model=schema.Message)
async def PushMsg(message: schema.Message, db:  db_dependency):
    query = model.Message(**message.model_dump())
    try:
        db.add(query)
        db.commit()
        # db.refresh()
        return query
    except Exception as err:
        return err

@app.get("/items")
async def printItem(*, name: str | None = None, channelId: int | None = None, accountId: int | None = None, db: db_dependency):
    post = db.query(model.Channel).filter(model.Channel.Name == name).all()

    return post


