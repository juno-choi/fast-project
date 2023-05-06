from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_service

router = APIRouter(
    prefix="/v1/question",
)

@router.get("/list", response_model=list[question_schema.Question])
def list(db: Session = Depends(get_db)):
    _question_list = question_service.get_question_list(db)
    return _question_list