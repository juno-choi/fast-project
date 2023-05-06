from sqlalchemy.orm import Session

from models import Question

def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_at.desc())\
        .all()
    return question_list
        