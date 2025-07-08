from entity import *
from entity.user import User


def add_user(user):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        return e
    
def get_user_byID(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return user
        return None
    except Exception as e:
        return e
def get_user(filters:dict,page:int = None,page_size:int = None):
    try:
        res = User.query
        if filters:
            res = User.query.filter_by(**filters)
        if page:
            page = int(page)
        if page_size:
            page_size = int(page_size)
        res = res.paginate(page=page, per_page=page_size).items
        r = []
        for i in res:
            r.append(i.to_dict())
        return r
    except Exception as e:
        return e
    
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return user.to_dict()
        return False
    except Exception as e:
        return e
    
def update_user(user:User):
    try:
        update_user = User.query.filter_by(id=user.id).first()
        if not update_user:
            return None
        for key,value in user.to_dict().items():
            if hasattr(user,key) and getattr(user,key):
                setattr(update_user,key,value)
        update_user.update_time = datetime.datetime.now()
        db.session.commit()
        return update_user.to_dict()
    except Exception as e:
        return e