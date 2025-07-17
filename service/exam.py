import datetime
from entity.exam import Exam
from data.exam import add, get, update
from utils.response import Response


class ExamService:
    def __init__(self):
        pass
    def create_exam(self,user_id,date1,date2):
        return Exam(
            user_id = user_id,
            date1 = datetime.datetime.fromisoformat(date1.replace('Z', '')),
            date2 = datetime.datetime.fromisoformat(date2.replace('Z', ''))
        )

    #更新两个考试日期
    def updateExam(self,user_id,date1,date2):
        try:
            if not user_id or not date1 or not date2:
                return Response.NOT_FOUND("更新数据不能为空")
            exam = self.create_exam(user_id,date1,date2)
            
            if not get(user_id):
                res = add(exam)
                if isinstance(res,Exception):
                    return Response.SEVER_ERROR(res)
            res = update(exam)
            if isinstance(res,Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(res)
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    def getExam(self,user_id):
        try:
            if not user_id:
                return Response.NOT_FOUND("用户ID不能为空")
            res = get(user_id)
            if isinstance(res,Exception):
                return Response.SEVER_ERROR(res)
            if not res:
                return Response.NOT_FOUND("没有考试计划")
            return Response.SUCCESS(res)
        except Exception as e:
            return Response.SEVER_ERROR(e)

