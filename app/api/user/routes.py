from flask import Blueprint

user_blueprint = Blueprint('user', __name__, url_prefix='/user')

"""
Create CRUD for user

GET /user - Get all users
POST /user - Add user

GET /user/<id> - Get user by id
PUT /user/<id> - Update user by id
DELETE /user/<id> - Delete user by id


"""
#
# @user_blueprint.route('/test')
# def test():
#     return 'test'