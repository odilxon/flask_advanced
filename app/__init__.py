from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager


db = SQLAlchemy()
admin = Admin(name="Home", template_mode='bootstrap4')

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('configs/main.py')

    from app.api.routes import api_blueprint
    from app.api2.routes import api2
    from app.pages.routes import pages_blueprint
    app.register_blueprint(api_blueprint)
    app.register_blueprint(pages_blueprint)
    app.register_blueprint(api2)
    db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'pages.login'

    from app.model import User, Post
    from app.adminviews import MyModelView

    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Post, db.session))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    @app.errorhandler(404)
    def page_not_found(e):
        return {'error': 'page not found'}
    return app