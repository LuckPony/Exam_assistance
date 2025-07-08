from __init__ import *

class Plan(db.Model):
    """ 计划表
     id:计划id
     name:计划名称
     description:计划描述
     finished:计划是否完成
     create_time:计划创建时间
     update_time:计划更新时间
     deal_time:计划截止时间
       """
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    finished = db.Column(db.Boolean, nullable=False, default=False)
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    deal_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return '<Plan %r>' % self.name
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'finished': self.finished,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'deal_time': self.deal_time
        }