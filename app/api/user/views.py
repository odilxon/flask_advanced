from flask.views import MethodView
from app.model import User
from flask import request, jsonify
from app import db

"""
Create CRUD for user

GET /user - Get all users
POST /user - Add user

GET /user/<id> - Get user by id
PUT /user/<id> - Update user by id
DELETE /user/<id> - Delete user by id


"""


class UserAPIById(MethodView):
    def get(self, id):
        us = User.query.get_or_404(id)
        return jsonify(us.format())

    def put(self, id):
        us = User.query.get_or_404(id)
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        us.username = username
        us.password = password
        us.email = email
        db.session.add(us)
        db.session.commit()
        return jsonify(us.format())

    def delete(self, id):
        us = User.query.get_or_404(id)
        db.session.delete(us)
        db.session.commit()
        return jsonify({'success': 'delete'})


class UserAPI(MethodView):
    def get(self):
        users = User.query.all()
        return jsonify([us.format() for us in users])

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        us = User(username=username, password=password, email=email)
        db.session.add(us)
        db.session.commit()
        return jsonify(us.format())
