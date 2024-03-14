from sqlalchemy.orm import Session

import models, schemas

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item: schemas.Item):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db_item.title = item.title
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item

def create_country(db: Session, country: schemas.CountryCreate):
    db_country = models.Country(**country.dict())
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()

def get_countries(db: Session):
    return db.query(models.Country).all()

def update_country(db: Session, country_id: int, country: schemas.CountryCreate):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    for key, value in country.dict().items():
        setattr(db_country, key, value)
    db.commit()
    db.refresh(db_country)
    return db_country

def delete_country(db: Session, country_id: int):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    db.delete(db_country)
    db.commit()
    return db_country

def create_supermarket(db: Session, supermarket: schemas.SupermarketCreate):
    db_supermarket = models.Supermarket(**supermarket.dict())
    db.add(db_supermarket)
    db.commit()
    db.refresh(db_supermarket)
    return db_supermarket

def get_supermarket(db: Session, supermarket_id: int):
    return db.query(models.Supermarket).filter(models.Supermarket.id == supermarket_id).first()

def get_supermarkets(db: Session):
    return db.query(models.Supermarket).all()

def update_supermarket(db: Session, supermarket_id: int, supermarket: schemas.SupermarketCreate):
    db_supermarket = db.query(models.Supermarket).filter(models.Supermarket.id == supermarket_id).first()
    for key, value in supermarket.dict().items():
        setattr(db_supermarket, key, value)
    db.commit()
    db.refresh(db_supermarket)
    return db_supermarket

def delete_supermarket(db: Session, supermarket_id: int):
    db_supermarket = db.query(models.Supermarlet).filter(models.Supermarket.id == supermarket_id).first()
    db.delete(db_supermarket)
    db.commit()
    return db_supermarket
