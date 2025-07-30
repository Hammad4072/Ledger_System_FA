from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter(
    prefix="/ledger",
    tags=["Ledger"]
)

@router.get("/balance")
def get_balance(db: Session = Depends(database.get_db)):
    total_income = db.query(models.Transaction).filter(models.Transaction.type == "income").with_entities(models.Transaction.amount).all()
    total_expense = db.query(models.Transaction).filter(models.Transaction.type == "expense").with_entities(models.Transaction.amount).all()

    income_sum = sum([i[0] for i in total_income])
    expense_sum = sum([e[0] for e in total_expense])

    return {"balance": income_sum - expense_sum}