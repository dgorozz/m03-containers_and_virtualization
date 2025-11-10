import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import logging

from .database import get_db, Base, engine

from . import models
from . import schemas
from . import crud


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s"
)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/dogs", response_model=list[schemas.DogResponse])
def get_dogs(db: Session = Depends(get_db)):
    dogs: list[models.Dog] = crud.get_all_dogs(db)
    logger.info(f"Dog list returned. Length={len(dogs)}")
    return dogs


@app.get("/dogs/{dog_id}", response_model=schemas.DogResponse)
def get_dog(dog_id: int, db: Session = Depends(get_db)):
    dog = crud.get_dog_by_id(db, dog_id)
    if not dog:
        logger.error(f"Dog with id {dog_id} not found")
        raise HTTPException(status_code=404, detail=f"Dog with id {dog_id} not found")
    logger.info(f"Returned dog with id {dog.id}")
    return dog


@app.post("/dogs", response_model=schemas.DogResponse)
def create_dog(dog: schemas.DogCreate, db: Session = Depends(get_db)):
    db_dog = crud.create_dog(db, dog)
    logger.info(f"Dog created with id {db_dog.id}")
    return db_dog


@app.delete("/dogs/{dog_id}", status_code=204)
def remove_dog(dog_id: int, db: Session = Depends(get_db)):
    is_deleted = crud.delete_dog(db, dog_id)
    if not is_deleted:
        logger.error(f"Dog with id {dog_id} not found")
        raise HTTPException(status_code=404, detail=f"Dog with id {dog_id} not found")
    logger.info(f"Dog with id {dog_id} deleted from database")
    return



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8000")