from flask import Blueprint

from app.core import token_required

from .user.views import UserAPIById, UserAPI

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
# api_blueprint.register_blueprint(user_blueprint)

api_blueprint.add_url_rule('/user/<int:id>', view_func=token_required(UserAPIById.as_view('user_by_id')))
api_blueprint.add_url_rule('/user', view_func=UserAPI.as_view('user'))


