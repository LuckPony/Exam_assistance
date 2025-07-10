from flask import request
from flask_restx import Namespace, Resource,fields

from service.reflection import reflectionService
from utils.response import Response

reflection_ns = Namespace('api/reflection', description='反思记录管理')

reflection_model = reflection_ns.model('reflection', {
    'id': fields.Integer(required=False,default = 0, description='反思记录ID'),
    'content': fields.String(required=False, description='反思内容'),
    'plan_id': fields.Integer(required=False, description='反思的计划ID'),

})

paper_parser = reflection_ns.parser()
paper_parser.add_argument('plan_id', type=int, required=False, help='请输入反思计划ID')
paper_parser.add_argument('content', type=str, required=False, help='请输入反思内容')
paper_parser.add_argument('create_time', type=str, required=False, help='请输入反思创建时间')
paper_parser.add_argument('update_time', type=str, required=False, help='请输入反思更新时间')
paper_parser.add_argument('page', type=int, required=False, default=1  ,help='页码')
paper_parser.add_argument('page_size', type=int, required=False, default=10 ,help='每页条数')

@reflection_ns.route('/<string:id>')
class Reflection(Resource):

    @reflection_ns.expect(reflection_model)
    def post(self,id):
        """添加反思记录"""
        try:
            data = request.get_json()
            if not data or not data.get('content') or not data.get('plan_id'):
                return Response.NOT_FOUND("反思内容、计划ID不能为空")
            return reflectionService().add(data)
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    
    def delete(self,id):
        """删除反思记录"""
        try:
            if not id:
                return Response.NOT_FOUND("id不能为空")
            return reflectionService().delete(id)
        except Exception as e:
            return Response.SEVER_ERROR(e)

    @reflection_ns.expect(reflection_model)
    def put(self,id):
        """更新反思记录"""
        try:
            data = request.get_json()
            if not data or not id:
                return Response.NOT_FOUND("id不能为空")
            return reflectionService().update(id,data)
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
@reflection_ns.route('/')
class ReflectionDetail(Resource):
    @reflection_ns.expect(paper_parser)
    def get(self):
        """获取反思记录列表"""
        try:
            args = paper_parser.parse_args()
            filters = {}
            for key,value in args.items():
                if getattr(args,key) and key != 'page' and key != 'page_size':
                    filters[key] = value
            return reflectionService().getReflectionList(filters, args.get('page'), args.get('page_size'))
        except Exception as e:
            return Response.SEVER_ERROR(e)
            
            
    
