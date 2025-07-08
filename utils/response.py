
from flask import jsonify


class Response:
    def __init__(self, code, message, data=None):
        self.code = code
        self.message = message
        self.data = data

    def to_dict(self):
        return jsonify({  #转换为json格式
            'code': self.code,
            'message': self.message,
            'data': self.data
        })
    @staticmethod   #装饰器用来定义静态方法，此时不需要实例化对象，也不会自动传入 self。
    def SUCCESS(data):
        """请求成功"""
        return Response(200, 'success', data if data else None).to_dict()

    @staticmethod
    def SEVER_ERROR(e):
        """服务器错误"""
        return Response(500, "internal server error",str(e) if e else None).to_dict()
    
    @staticmethod
    def NOT_FOUND(string):
        """资源未找到"""
        return Response(404, f"{string}").to_dict()