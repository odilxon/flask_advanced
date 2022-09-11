from flask.views import MethodView
from flask import request, jsonify
from app import db

class ItemViewByID(MethodView):

    def __init__(self, model):
        self.model = model

    def get(self, id):
        res = self.model.query.get_or_404(id)
        return res.to_dict()

    def put(self, id):
        item = self.model.query.get_or_404(id)
        return item.update(request)


    def delete(self, id):
        item = self.model.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return jsonify({'success': 'delete'})

class ItemView(MethodView):

    def __init__(self, model):
        self.model = model

    def get(self):
        res = self.model.query.all()
        return jsonify([item.to_dict() for item in res])

    def post(self):

        res = self.model.insert(self.model, request)

        return jsonify({"success" : res})