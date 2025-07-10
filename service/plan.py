from flask import json
from data.plan import *
from entity import *
from utils.response import Response

class PlanService:
    def __init__(self):
        pass
    def create_plan_object(self, data):  #这里创建对象只是为了更好传信息，所以无用字段可不加
        return Plan(
            planname = data.get('planname'),
            description = data.get('description'),
            begin_time =  datetime.datetime.fromisoformat(data.get('begin_time').replace('Z', '')),
            deal_time =  datetime.datetime.fromisoformat(data.get('deal_time').replace('Z', '')),
            finished = data.get('finished'),
        )
    
    def add(self, data):
        try:
            plan = self.create_plan_object(data)
            
            res = add_plan(plan)
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            print("测试一下")
            print(plan)
            return Response.SUCCESS(f"成功添加计划{plan.to_dict()}")
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    def delete(self, id):
        try:
            res = delete_plan(id)
            if not res:
                return Response.NOT_FOUND('没有该计划')
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(f"成功删除id为{id}的计划")
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    def update(self, id,data):
        try:
            
            plan = self.create_plan_object(data)
            plan.id = id
            res = update_plan(plan)
            if not res:
                return Response.NOT_FOUND('没有该计划')
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(f"成功更新id为{plan.id}的计划{plan.planname}")
        except Exception as e:
            return Response.SEVER_ERROR(e)
    def getPlanList(self,filters:dict,page:int = None,page_size:int = None):
        try:
            res = get_plan(filters,page,page_size)
            if not res:
                return Response.NOT_FOUND('没有计划')
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            
            return Response.SUCCESS(res)
        except Exception as e:
            return Response.SEVER_ERROR(e)