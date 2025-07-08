from entity import *
class User(db.Model):
    """"用户表
    id: 用户id
    username: 用户名
    password: 密码
    phone:手机号
    email: 邮箱
    role: 角色
    update_time: 更新时间
    create_time: 创建时间
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)#autoincrement标识字段是自增的
    username = db.Column(db.String(64),)
    password = db.Column(db.String(64), )
    phone = db.Column(db.String(64), )
    email = db.Column(db.String(64), )
    role = db.Column(db.String(64), )
    update_time = db.Column(db.DateTime, default=datetime.datetime.now())
    create_time = db.Column(db.DateTime,  default=datetime.datetime.now())

    def __repr__(self):#打印对象时显示
        return '<User %r %r>' % self.id % self.username
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'phone': self.phone,
            'email': self.email,
            'role': self.role,
            'update_time': self.update_time,
            'create_time': self.create_time
        }