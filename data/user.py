from entity import *


def add_user(user):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        return e