

from data.user import add_user
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
            return Response.SUCCESS(data)
        except Exception as e:
            return Response.SEVER_ERROR(e)
