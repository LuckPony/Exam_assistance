from entity.reflection import PlanReflection
from entity import *

def add_reflection(reflection:PlanReflection):
    try:
        db.session.add(reflection)
        db.session.commit()
        return reflection.to_dict()
    except Exception as e:
        return e
    
def delete_reflection(id):
    try:
        reflection = PlanReflection.query.filter_by(id=id).first()
        if not reflection:
            return None
        db.session.delete(reflection)
        db.session.commit()
        return True
    except Exception as e:
        return e
    
def update_reflection(reflection:PlanReflection):
    try:
        update_reflection = PlanReflection.query.filter_by(id=reflection.id).first()
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
def get_reflection(filters:dict,page:int = None,page_size:int = None):
    try:
        reflection = PlanReflection.query
        if filters:
            reflection = reflection.filter_by(**filters)
        if not reflection:
            return None
        if page:
            page = int(page)
        if page_size:
            page_size = int(page_size)
        reflection = reflection.paginate(page=page,per_page=page_size).items
        r=[]
        for i in reflection:
            r.append(i.to_dict())
        return r
    except Exception as e:
        return e
