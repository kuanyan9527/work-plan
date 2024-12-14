from flask import Blueprint

bp = Blueprint('my_blueprint', __name__)

@bp.route('/')
def hello_world():
  return 'hello world\n'