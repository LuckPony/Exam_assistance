from flask import Flask
from config.sql import SQLConfig
from entity import *
from api import api
def create_app():
    app = Flask(__name__)
    app.config.from_object(SQLConfig)
    db.init_app(app)
    api.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    # 数据库迁移用：首次运行先创建表
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=True)
