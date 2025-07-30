from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/transaction", tags=["Transaction"])

get_db_session = Depends(database.get_db)


@router.post("/add")
def create_transaction(
    transaction: schemas.TransactionCreate,
    db: Session = get_db_session,
):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@router.get("/all")
def get_transactions(db: Session = get_db_session):
    return db.query(models.Transaction).all()
