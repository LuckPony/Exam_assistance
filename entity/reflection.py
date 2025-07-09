from __init__ import *

class Reflection:
    """每日反思
    id:反思的标识ID
    content:反思的内容
    plan_id:反思所对应的计划ID
    create_time:反思日期
    update_time:更新日期
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1024), nullable=False)
    plan_id = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return f"<Reflection {self.id}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "plan_id": self.plan_id,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        }