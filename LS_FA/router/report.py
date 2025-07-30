from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date
from datetime import datetime, timedelta
from .. import models, database

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.get("/daily")
def get_daily_report(db: Session = Depends(database.get_db)):
    today = datetime.utcnow().date()
    transactions = db.query(models.Transaction).filter(cast(models.Transaction.date, Date) == today).all()
    return transactions


@router.get("/weekly")
def get_weekly_report(db: Session = Depends(database.get_db)):
    today = datetime.utcnow().date()
    week_ago = today - timedelta(days=7)
    transactions = db.query(models.Transaction).filter(models.Transaction.date >= week_ago).all()
    return transactions