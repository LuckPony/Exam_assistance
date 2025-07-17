from entity.exam import Exam
from entity import *
def add(exam:Exam):
    try:
        db.session.add(exam)
        db.session.commit()
        return exam
    except Exception as e:
        return e
    
def update(exam:Exam):
    try:
        update_exam = Exam.query.filter_by(user_id=exam.user_id).first()
        if not update_exam:
            return None
        for key,value in exam.to_dict().items():
            if hasattr(exam,key) and getattr(exam,key):
                setattr(update_exam,key,value)
        update_exam.update_time = datetime.datetime.now()
        db.session.commit()
        return update_exam.to_dict()
    except Exception as e:
        return e
    
def get(user_id):
    try:
        if not user_id:
            return None
        exam = Exam.query.filter_by(user_id=user_id).first()
        if not exam:
            return None
        return exam.to_dict()
    except Exception as e:
        return e

        