from entity import *
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
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