from flask.views import MethodView
from flask import jsonify, request
from flaskr.model.ads import ads_collection


class FacebookAdView(MethodView):
    def get_object(self, name):
        return ads_collection.find_one({'name':name})

    def get(self):
        name = request.args.get('name', None)
        if not name:
            return jsonify({'error':'data not found'}), 404
        else:
            ad = self.get_object(name)
            response_data = {
                'name': ad['name'],
                'bio': ad['bio'],
                'tags':ad['tags']
            }
            return jsonify(response_data), 200

    def post(self):
        request_data = request.json
        ads_collection.insert_one({'name': request_data['name']})
        return jsonify({'result': 'success'}), 201

    def put(self, pk):
        name = request.args.get('name', None)
        if not name:
            return jsonify({'error': 'data not found'}), 404
        else:
            ads_collection.update_one({"name": name}, {"$set": {"name": "holy"}})

    def delete(self):
        name = request.args.get('name', None)
        if not name:
            return jsonify({'error':'data not found'}), 404
        else:
            ads_collection.delete_one({"name": name})
