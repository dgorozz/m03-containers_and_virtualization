from sqlalchemy.orm import Session
from . import models
from . import schemas

def get_dog_by_id(db: Session, dog_id: int):
    return db.query(models.Dog).filter(models.Dog.id == dog_id).first()

def get_all_dogs(db: Session):
    return db.query(models.Dog).all()

def create_dog(db: Session, dog: schemas.DogCreate):
    db_dog = models.Dog(name=dog.name, age=dog.age)
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

def delete_dog(db: Session, dog_id: int):
    db_dog = get_dog_by_id(db, dog_id)
    if not db_dog:
        return None

    db.delete(db_dog)
    db.commit()
    return True