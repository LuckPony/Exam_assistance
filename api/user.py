from flask import request
from flask_restx import Namespace, Resource,fields

from service.user import UserService
from utils.response import Response


user_ns = Namespace('api/user', description='用户管理')

register_model = user_ns.model('register', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码'),
    'email': fields.String(required=False, description='邮箱'),
    'phone': fields.String(required=False, description='手机号'),
})
login_model = user_ns.model('login', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码'),
})

user_model = user_ns.model('user', {
    'id': fields.Integer(required=True, description='用户ID'),
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码'),
    'email': fields.String(required=False, description='邮箱'),
    'phone': fields.String(required=False, description='手机号'),
})
paper_parser = user_ns.parser()
paper_parser.add_argument('username', type=str, required=False, help='用户名')
paper_parser.add_argument('email', type=str, required=False, help='邮箱')
paper_parser.add_argument('phone', type=str, required=False, help='手机号')
paper_parser.add_argument('page', type=int, required=False,default=1, help='页码')
paper_parser.add_argument('size', type=int, required=False,default=10 ,help='每页数量')


@user_ns.route('/register')
class UserRegister(Resource):
    @user_ns.expect(register_model)
    def post(self):
        """用户注册"""
        try:
            data = request.get_json()
            if not data or not data.get('username') or not data.get('password') or not data.get('email'):
                return Response.NOT_FOUND("用户名、密码、邮箱为空")
            return UserService().register(data)
        except Exception as e:
            return Response.SEVER_ERROR(e)

@user_ns.route('/login')
class UserLogin(Resource):
    @user_ns.expect(login_model)
    def post(self):
        """用户登录"""
        try:
            data = request.get_json()
            if not data or not data.get('username') or not data.get('password'):
                return Response.NOT_FOUND("用户名、密码为空")
            return UserService().login(data.get('username'), data.get('password'))
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
@user_ns.route('/<string:id>')
class User(Resource):
    def delete(self,id):
        """删除用户"""
        try:
            if not id:
                return Response.NOT_FOUND("用户ID为空")
            return UserService().delete(id)
        except Exception as e:
            return Response.SEVER_ERROR(e)

    @user_ns.expect(user_model)
    def put(self,id):
        """更新用户"""
        try:
            data = request.get_json()
            if not data or not id:
                return Response.NOT_FOUND("要修改的用户ID为空")
            return UserService().update(id,data)
        except Exception as e:
            return Response.SEVER_ERROR(e)
@user_ns.route('/')
class UserDetail(Resource):
    @user_ns.expect(paper_parser)
    def get(self):
        """获取用户列表"""
        try:
            args = paper_parser.parse_args()
            filters = {}
            for key,value in args.items():
                if getattr(args,key) and key != 'page' and key != 'size':
                    filters[key] = value
            print(filters)
            return UserService().getUserList(filters,args.get('page'),args.get('size'))
        except Exception as e:
            return Response.SEVER_ERROR(e)

            
                
            