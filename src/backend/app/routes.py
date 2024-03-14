from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/", response_model=schemas.Item, tags=["items"])
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.create_item(db=db, item=item)
    return db_item

@router.get("/items/", response_model=list[schemas.Item], tags=["items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/items/{item_id}", response_model=schemas.Item, tags=["items"])
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/items/{item_id}", response_model=schemas.Item, tags=["items"])
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id=item_id, item=item)
    return db_item

@router.delete("/items/{item_id}", response_model=schemas.Item, tags=["items"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id=item_id)
    return db_item

@router.post("/places/", response_model=schemas.Place, tags=["places"])
def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = crud.create_place(db=db, place=place)
    return db_place

@router.get("/places/", response_model=list[schemas.Place], tags=["places"])
def read_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places(db, skip=skip, limit=limit)
    return places

@router.get("/places/{place_id}", response_model=schemas.Place, tags=["places"])
def read_place(place_id: int, db: Session = Depends(get_db)):
    db_place = crud.get_place(db, place_id=place_id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place

@router.put("/places/{place_id}", response_model=schemas.Place, tags=["places"])
def update_place(place_id: int, place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = crud.update_place(db, place_id=place_id, place=place)
    return db_place

@router.delete("/places/{place_id}", response_model=schemas.Place, tags=["places"])
def delete_place(place_id: int, db: Session = Depends(get_db)):
    db_place = crud.delete_place(db, place_id=place_id)
    return db_place

@router.post("/countries/", response_model=schemas.Country, tags=["countries"])
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    db_country = crud.create_country(db=db, country=country)
    return db_country

@router.get("/countries/", response_model=list[schemas.Country], tags=["countries"])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = crud.get_countries(db, skip=skip, limit=limit)
    return countries

@router.get("/countries/{country_id}", response_model=schemas.Country, tags=["countries"])
def read_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country

@router.put("/countries/{country_id}", response_model=schemas.Country, tags=["countries"])
def update_country(country_id: int, country: schemas.CountryCreate, db: Session = Depends(get_db)):
    db_country = crud.update_country(db, country_id=country_id, country=country)
    return db_country

@router.delete("/countries/{country_id}", response_model=schemas.Country, tags=["countries"])
def delete_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.delete_country(db, country_id=country_id)
    return db_country

@router.post("/supermarkets/", response_model=schemas.Supermarket, tags=["supermarkets"])
def create_supermarket(supermarket: schemas.SupermarketCreate, db: Session = Depends(get_db)):
    db_supermarket = crud.create_supermarket(db=db, supermarket=supermarket)
    return db_supermarket

@router.get("/supermarkets/", response_model=list[schemas.Supermarket], tags=["supermarkets"])
def read_supermarkets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    supermarkets = crud.get_supermarkets(db, skip=skip, limit=limit)
    return supermarkets

@router.get("/supermarkets/{supermarket_id}", response_model=schemas.Supermarket, tags=["supermarkets"])
def read_supermarket(supermarket_id: int, db: Session = Depends(get_db)):
    db_supermarket = crud.get_supermarket(db, supermarket_id=supermarket_id)
    if db_supermarket is None:
        raise HTTPException(status_code=404, detail="Supermarket not found")
    return db_supermarket

@router.put("/supermarkets/{supermarket_id}", response_model=schemas.Supermarket, tags=["supermarkets"])
def update_supermarket(supermarket_id: int, supermarket: schemas.SupermarketCreate, db: Session = Depends(get_db)):
    db_supermarket = crud.update_supermarket(db, supermarket_id=supermarket_id, supermarket=supermarket)
    return db_supermarket

@router.delete("/supermarkets/{supermarket_id}", response_model=schemas.Supermarket, tags=["supermarkets"])
def delete_supermarket(supermarket_id: int, db: Session = Depends(get_db)):
    db_supermarket = crud.delete_supermarket(db, supermarket_id=supermarket_id)
    return db_supermarket

