from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import schemas, crud
from backend.database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


get_db_dependency = Depends(get_db)


@router.post("/")
def create_user(
    user: schemas.UserCreate,
    db: Session = get_db_dependency,
):
    return crud.create_user(db, user)
