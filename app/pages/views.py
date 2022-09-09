from flask.views import MethodView
from app.model import User
from flask import request, redirect, url_for, render_template
from flask_login import login_user

class LoginView(MethodView):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        next = request.form.get('next')

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(next)
        return redirect(url_for('pages.login'))

    def get(self):
        next = request.args.get('next')
        return render_template('login.html', next=next)