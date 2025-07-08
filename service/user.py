

from data.user import *
from entity.user import *
from utils.response import Response


class UserService:
    def __init__(self):
        pass

    def create_user_object(self, data):
        return User(
            username = data.get('username'),
            password = data.get('password'),
            phone = data.get('phone'),
            email = data.get('email'),
        )

    def register(self, data):
        try:
            user = self.create_user_object(data)
            res = add_user(user)
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(f"成功注册用户{data}")
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    def login(self, username:str, password:str):
        try:
            user = get_user(filters={'username':username, 'password':password})
            if isinstance(user, Exception):
                return Response.SEVER_ERROR(user)
            if not user: 
                return Response.NOT_FOUND("用户不存在")
            return Response.SUCCESS(f"用户登录成功{user}")
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    def delete(self, id):
        try:
            res = delete_user(id)
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            if res == False: 
                return Response.NOT_FOUND("用户不存在")
            return Response.SUCCESS(f"成功删除id为{id}的用户")
        except Exception as e:
            return Response.SEVER_ERROR(e)
        
    def update(self,data):
        try:
            user = self.create_user_object(data) #创建用户对象时id是自动生成的
            user.id = data.get('id')
            res = update_user(user)
            if res == None: 
                return Response.NOT_FOUND("用户不存在")
            if isinstance(res, Exception):
                return Response.SEVER_ERROR(res)
            return Response.SUCCESS(f"用户更新成功{res}")
        except Exception as e:
            return Response.SEVER_ERROR(e)
    def getUserList(self,filters:dict,page:int = None,page_size:int = None):
        try:
            user = get_user(filters,page,page_size)
            if not user: 
                return Response.NOT_FOUND("没有用户符合条件")
            if isinstance(user, Exception):
                return Response.SEVER_ERROR(user)
            return Response.SUCCESS(f"用户查询成功{user}")
        except Exception as e:
            return Response.SEVER_ERROR(e)




        
