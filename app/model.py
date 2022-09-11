from app import db
from flask_login import UserMixin
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def update(self, request):
        self.username = request.form.get('username', self.username)
        self.password = request.form.get('password', self.password)
        self.email = request.form.get('email', self.email)
        self.save()
        return True

    @staticmethod
    def insert(model, request):
        user = model()
        user.username = request.form.get('username')
        user.password = request.form.get('password')
        user.email = request.form.get('email')
        user.save()
        return True



class Post(BaseModel):
    __tablename__ = 'post'
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def update(self, request):
        self.title = request.form.get('title', self.title)
        self.content = request.form.get('content', self.content)
        self.user_id = request.form.get('user_id', self.user_id)
        self.save()
        return self.to_dict()
    def __repr__(self):
        return '<Post %r>' % self.title

    @staticmethod
    def insert(model, request):
        post = model()
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.user_id = request.form.get('user_id')
        post.save()
        return True