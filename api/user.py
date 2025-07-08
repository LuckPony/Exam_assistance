from flask import request
from flask_restx import Namespace, Resource,fields

from service.user import UserService
from utils.response import Response


user_ns = Namespace('api/user', description='用户管理')

user_model = user_ns.model('User', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码'),
    'email': fields.String(required=True, description='邮箱'),
    'phone': fields.String(required=True, description='手机号'),
})


@user_ns.route('/')
class UserApi(Resource):
    @user_ns.expect(user_model)
    def post(self):
        """注册用户"""
        try:
            data = request.get_json()
            if not data or not data.get('username') or not data.get('password') or not data.get('email'):
                return Response.NOT_FOUND()
            return UserService().register(data)
        except Exception as e:
            return Response.SEVER_ERROR(e)
            
                
            