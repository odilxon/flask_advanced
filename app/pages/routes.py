from flask import Blueprint
from .views import LoginView
pages_blueprint = Blueprint('pages', __name__, url_prefix="/pages",template_folder='templates')


pages_blueprint.add_url_rule('/login', view_func=LoginView.as_view('login'))