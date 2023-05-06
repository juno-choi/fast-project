from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Question

router = APIRouter(
    prefix="/v1/question",
)

@router.get("/list")
def list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_at.desc()).all()
    return _question_list