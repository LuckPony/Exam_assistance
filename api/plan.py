from flask import request
from flask_restx import Namespace, Resource,fields

from service.plan import PlanService
from utils.response import Response


plan_ns = Namespace('api/plan',description='计划管理')

plan_model = plan_ns.model('plan', {
    'id': fields.Integer(required=False,default=0 ,description='计划id'),
    'planname': fields.String(required=False, description='计划名称'),
    'description': fields.String(required=False, description='计划描述'),
    'begin_time': fields.DateTime(required=False, description='计划开始时间'),
    'deal_time': fields.DateTime(required=False, description='计划截止时间'),
    'finished': fields.Boolean(required=False,default=False,description='计划是否完成'),
    'user_id': fields.Integer(required=False, description='用户ID'),
})

paper_parser = plan_ns.parser()

paper_parser.add_argument('planname', type=str, required=False, help='计划名称')
paper_parser.add_argument('begin_time', type=str, required=False, help='计划开始时间')
paper_parser.add_argument('deal_time', type=str, required=False, help='计划截止时间')
paper_parser.add_argument('finished', type=bool, required=False,default=False ,help='计划是否完成')
paper_parser.add_argument('user_id', type=int, required=False, help='计划所有者id')
paper_parser.add_argument('page', type=int, required=False, default=1  ,help='页码')
paper_parser.add_argument('size', type=int, required=False, default=10 ,help='每页数量')


@plan_ns.route('/<string:id>')
class Plan(Resource):
    @plan_ns.expect(plan_model)
    def post(self,id):
        """添加计划"""
        try:
            data = request.get_json()
            if not data or not data.get('planname') or not data.get('description') or not data.get('begin_time') or not data.get('deal_time'):
                return Response.NOT_FOUND("计划名、计划项、计划开始和结束时间不能为空");
            return PlanService().add(data)
        except Exception as e:
            return Response.SEVER_ERROR(e)
    

    def delete(self,id):
        """"删除计划"""
        try:
            if not id:
                return Response.NOT_FOUND("计划id不能为空");
            return PlanService().delete(id)
        except Exception as e:
            return Response.SEVER_ERROR(e)

    @plan_ns.expect(plan_model)
    def put(self,id):
        """更新计划"""
        try:
            data = request.get_json()
            if not id:
                return Response.NOT_FOUND("要更新的计划id不能为空");
            return PlanService().update(id,data)
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
@plan_ns.route('/')
class PlanDeatil(Resource):
    @plan_ns.expect(paper_parser)
    def get(self):
        """获取计划列表"""
        try:
            args = paper_parser.parse_args()
            filters = {}
            for key,value in args.items():
                if getattr(args,key) and key != 'page' and key != 'size':
                    filters[key] = value
            return PlanService().getPlanList(filters, args.get('page'), args.get('size'))
        except Exception as e:
            return Response.SEVER_ERROR(e)


