
from data.reflection import *
from entity.reflection import PlanReflection
from utils.response import Response


class reflectionService:
    def __init__(self):
        pass
    def create_reflection_object(self, data):
        return PlanReflection(
            content = data.get('content'),
            plan_id = data.get('plan_id'),
        )

    def add(self, data):
        try:
            if not data or not data.get('content'):
                return Response.NOT_FOUND('反思内容不能为空')
            reflection = self.create_reflection_object(data)
            res = add_reflection(reflection)
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(res)
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    def delete(self, id):
        try:
            res = delete_reflection(id)
            if not res:
                return Response.NOT_FOUND('该反思记录不存在')
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(res)
        except Exception as e:
            return Response.SEVER_ERROR(e)
    
    def update(self,data):
        try:
            if not data or not data.get('id'):
                return Response.NOT_FOUND('反思记录id不能为空')
            reflection = self.create_reflection_object(data)
            reflection.id = data.get('id')
            res = update_reflection(reflection)
            if not res:
                return Response.NOT_FOUND('该反思记录不存在')
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(res)
        except Exception as e:
            return Response.SEVER_ERROR(e)
    def getReflectionList(self,filters:dict,page:int = None,page_size:int = None):
        try:
            res = get_reflection(filters,page,page_size)
            if not res:
                return Response.NOT_FOUND('没有反思记录')
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(res)
        except Exception as e:
            return Response.SEVER_ERROR(e)
            