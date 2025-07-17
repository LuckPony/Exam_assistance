from flask import request
from flask_restx import Namespace, Resource,fields

from service.exam import ExamService
from utils.response import Response


exam_ns = Namespace('api/exam', description='考试信息管理')

exam_model = exam_ns.model('exam', {
    'id': fields.Integer(description='考试id'),
    'date1': fields.DateTime(description='考试1开始时间'),
    'date2': fields.DateTime(description='考试2开始时间'),
    'user_id': fields.Integer(description='用户id'),
})

paper_parser = exam_ns.parser()
paper_parser.add_argument('user_id', type=int, required=True, help='用户id')

@exam_ns.route('/')
class Exam(Resource):
    
    @exam_ns.expect(exam_model)
    def put(self):
        """更新考试日期信息"""
        try:
            data = request.get_json()
            user_id = data.get('user_id')
            date1 = data.get('date1')
            data2 = data.get('date2')
            if not user_id or not date1 or not data2:
                return Response.NOT_FOUND('输入不能为空')
            return ExamService().updateExam(user_id,date1,data2)
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    @exam_ns.expect(paper_parser)
    def get(self):
        """获取考试日期信息"""
        try:
            args = paper_parser.parse_args()
            user_id = args.get('user_id')
            if not user_id:
                return Response.NOT_FOUND('输入不能为空')
            return ExamService().getExam(user_id)
        except Exception as e:
            return Response.SEVER_ERROR(e)
