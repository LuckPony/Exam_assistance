from entity import *

class Exam(db.Model):
    """考试日期
    id: 考试ID
    date1: 考试1开始时间
    date2: 考试2开始时间
    user_id: 用户ID
    create_time: 创建时间
    update_time: 更新时间
    """
    __tablename__ = 'exam'
    id = db.Column(db.Integer, primary_key=True)
    date1 = db.Column(db.DateTime, nullable=False)
    date2 = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return f'<Exam {self.id}>'
    def to_dict(self):
        return {
            'id': self.id,
            'date1': self.date1,
            'date2': self.date2,
            'user_id': self.user_id,
            'create_time': self.create_time,
            'update_time': self.update_time
        }