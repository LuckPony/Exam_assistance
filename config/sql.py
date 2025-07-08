class SQLConfig:
    # Database connection details
    DB_HOST = "localhost"
    DB_PORT= 3306
    DB_USER = "root"
    DB_PASSWORD = "123456"
    DB_NAME = "examAssistance"

    #SQLAlchemy URI拼接
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
     # 关闭 SQLAlchemy 的修改追踪功能，节省内存
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否开启SQLAlchemy的调试日志
    SQLALCHEMY_ECHO = True
