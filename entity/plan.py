from entity import *

class Plan(db.Model):
    """ 计划表
     id:计划id
     planname:计划名称
     description:计划描述
     finished:计划是否完成
     begin_time:计划开始时间
     deal_time:计划截止时间
     user_id:计划创建者id
     create_time:创建时间
     update_time:更新时间
    
       """
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    planname = db.Column(db.String(100,collation='utf8mb4_general_ci'), nullable=False)
    description = db.Column(db.String(100,collation='utf8mb4_general_ci'), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    finished = db.Column(db.Boolean, nullable=False, default=False)
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    deal_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    begin_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Plan %r>' % self.id
    
    def to_dict(self):
        return {
            'id': self.id,
            'planname': self.planname,
            'description': self.description,
            'finished': self.finished,
            'begin_time': self.begin_time,  
            'deal_time': self.deal_time,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'user_id': self.user_id,
            
        }