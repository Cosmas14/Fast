from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create/")
def create_product(title:str,description:str,price:int,db:Session = Depends()):
    db_product = models.Shop(title=title,description=description,price=price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
