from flask_restx import Api
from .user import user_ns
from .plan import plan_ns
from .reflection import reflection_ns
def init_restx():
    api = Api(
        title="ExamAssistance API",
        version="1.0",
        description="API for ExamAssistance",
    )
    api.add_namespace(user_ns)
    api.add_namespace(plan_ns)
    api.add_namespace(reflection_ns)
    return api
    
api = init_restx()