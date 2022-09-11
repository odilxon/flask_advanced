from flask import Blueprint
from app.model import User, Post



api2 = Blueprint('api2', __name__, url_prefix='/api2')

from .views import ItemViewByID, ItemView


def register_routes(app, model, name):

    app.add_url_rule('/%s/<int:id>' % name, view_func=ItemViewByID.as_view('%s_id)' % name, model), methods=['GET', 'PUT', 'DELETE'])
    app.add_url_rule('/%s' % name, view_func=ItemView.as_view('%s_all)' % name, model),
                     methods=['GET', 'POST'])

register_routes(api2, User, 'user')
register_routes(api2, Post, 'post')