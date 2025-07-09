from entity.reflection import Reflection
from entity import *

def add_reflection(reflection:Reflection):
    try:
        db.session.add(reflection)
        db.session.commit()
        return reflection
    except Exception as e:
        return e
    
def delete_reflection(id):
    try:
        reflection = Reflection.query.filter_by(id=id).first()
        if not reflection:
            return None
        db.session.delete(reflection)
        db.session.commit()
        return True
    except Exception as e:
        return e
    
def update_reflection(reflection:Reflection):
    try:
        update_reflection = Reflection.query.filter_by(id=reflection.id).first()
        if not reflection:
            return None
        for key,value in reflection.to_dict().items():
            if hasattr(reflection,key) and getattr(reflection,key):
                setattr(update_reflection,key,value)
        update_reflection.update_time = datetime.datetime.now()
        db.session.commit()
        return update_reflection.to_dict()
    except Exception as e:
        return e
    
