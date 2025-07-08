from __init__ import *

class Reflection:
    """每日反思
    id:反思的标识ID
    create_time:反思的日期
    content:反思的内容
    plan_id:反思所对应的计划ID
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    plan_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Reflection {self.id}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "content": self.content,
            "plan_id": self.plan_id
        }