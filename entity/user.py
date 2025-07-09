from entity import *
class User(db.Model):
    """用户表
    id 用户id
    username 用户名
    password 密码
    phone 手机号
    email 邮箱
    role 角色
    update_time 更新时间
    create_time 创建时间
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80,collation='utf8mb4_general_ci'), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(64), )
    email = db.Column(db.String(64), )
    role = db.Column(db.String(64), )
    update_time = db.Column(db.DateTime, default=datetime.datetime.now()) #第一个datetime是模块，第二个是类，类中才有方法
    create_time = db.Column(db.DateTime,  default=datetime.datetime.now())

    def __repr__(self):#打印对象时显示
        return '<User %r>' % self.id
    
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