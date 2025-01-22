from flask import Blueprint

bp = Blueprint('work_plan_blueprint', __name__)

@bp.route('/')
def hello_world():
  return 'hello world\n'