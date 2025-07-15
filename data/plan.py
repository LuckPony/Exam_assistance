from sqlalchemy import func
from entity import *
from entity.plan import Plan

def add_plan(plan):
    try:
        db.session.add(plan)
        db.session.commit()
        return plan
    except Exception as e:
        return e
    
def delete_plan(id):
    try:
        plan = Plan.query.filter_by(id=id).first()
        if not plan:
            return None    
        db.session.delete(plan)
        db.session.commit()
        return True
    except Exception as e:
        return e
    
def update_plan(plan):
    try:
        update_plan = Plan.query.filter_by(id=plan.id).first()
        if not update_plan:
            return None
        for key,value in plan.to_dict().items():
            if hasattr(plan,key) and getattr(plan,key):
                setattr(update_plan,key,value)
        update_plan.update_time = datetime.datetime.now()
        db.session.commit()
        return plan.to_dict()
    except Exception as e:
        return e
    
def get_plan(filters:dict,page:int = None,page_size:int = None):
    try:
        res = Plan.query
        if filters:
            res = res.filter_by(**filters)
        if not res:
            return None
        if page:
            page = int(page)
        if page_size:
            page_size = int(page_size)
    
        r = []
        for i in res:
            r.append(i.to_dict())
        return r
    except Exception as e:
        return e
    
def get_plan_by_data(begin_month,deal_month,user_id):
    try:
        plans = Plan.query.filter_by(user_id=user_id)
        
        if begin_month and deal_month:
            plans = plans.filter(
                func.month(Plan.begin_time) == int(begin_month),
                func.month(Plan.deal_time) == int(deal_month),
                )
            print(plans)
        elif deal_month and not begin_month:
            plans = plans.filter(
                func.month(Plan.deal_time) == int(deal_month)
                )
        elif begin_month and not deal_month:
            plans = plans.filter(
                func.month(Plan.begin_time) == int(begin_month),
                )
        plans = plans.all()
        if not plans:
            return None
        r = []
        for i in plans:
            r.append(i.to_dict())
        return r
    except Exception as e:
        return e

