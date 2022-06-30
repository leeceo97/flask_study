from flask.views import MethodView
from flask import jsonify, request

from flaskr.model.ads import ads_collection


class FacebookAdView(MethodView):
    def get_object(self, name):
        return ads_collection.find_one({'name':name})

    def get(self):
        ads = ads_collection.find()
        response_data = []
        for ad in ads:
            _response_data = {
                'name': ad['name'],
            }
            response_data.append(_response_data)
        return jsonify(response_data), 200

    def post(self):
        request_data = request.json
        ads_collection.insert_one({'name': request_data['name']})
        return jsonify({'result': 'success'}), 201


class FacebookAdDetailView(MethodView):
    def get_object(self, name):
        return ads_collection.find_one({'name': name})

    def get(self, name):
        ad = self.get_object(name)
        if ad:
            response_data = {
                'name': ad['name'],
                'bio': ad['bio'],
                'tags': ad['tags'],
                'id': str(ad['_id']),
            }
            return jsonify(response_data), 200
        else:
            return jsonify({'error': 'data not found'}), 404

    def put(self, name):
        ad = self.get_object(name)
        request_data = request.json
        if not ad:
            return jsonify({'error': 'data not found'}), 404
        else:
            ads_collection.update_one({"name": name}, {"$set": {"name": request_data['name']}})

    def delete(self, name):
        ad = self.get_object(name)

        if not ad:
            return jsonify({'error': 'data not found'}), 404
        else:
            ads_collection.delete_one({"name": name})
            return jsonify({'message': 'delete success'}), 204
