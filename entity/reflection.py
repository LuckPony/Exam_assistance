from entity import *

class PlanReflection(db.Model):
    """每日反思

    id:反思的标识ID

    content:反思的内容

    plan_id:反思所对应的计划ID

    create_time:反思日期
    
    update_time:更新日期

    user_id:用户ID
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1024, collation='utf8mb4_general_ci'), nullable=False)
    plan_id = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    __tablename__ = "reflection"

    def __repr__(self):
        return f"<PlanReflection {self.id}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "plan_id": self.plan_id,
            "create_time": self.create_time,
            "create_time": self.create_time,
            'user_id': self.user_id
        }