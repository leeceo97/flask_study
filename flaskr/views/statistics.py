from flask.views import MethodView
from flask import jsonify, request

from flaskr.model.ads import ads_collection, FaceBookAds


class FacebookAdView(MethodView):
    def get_object(self, name):
        return ads_collection.find_one({'name':name})

    def get(self):
        _ads = FaceBookAds('test')
        ads = _ads.find_all()
        response_data = []
        for ad in ads:
            _response_data = {
                'name': ad['name'],
            }
            response_data.append(_response_data)
        return jsonify({'result':response_data}), 200

    def post(self):
        request_data = request.json
        db = FaceBookAds('test')
        a = db.insert_data(**request_data)
        return jsonify({'result': 'success'}), 201


class FacebookAdDetailView(MethodView):
    def get_object(self, name):
        return ads_collection.find_one({'name': name})

    def get(self, name):

        ad = self.get_object(name)
        if ad:
            response_data = {
                'name': ad['name'],
                #'bio': ad['bio'],
                #'tags': ad['tags'],
                #'id': str(ad['_id']),
            }
            return jsonify(response_data), 200
        else:
            return jsonify({'error': 'data not found'}), 404

    def put(self, name):
        ad = FaceBookAds('test')
        r_ad = ad.update_data('종이컵', '젖은 종이컵')
        return jsonify(r_ad)

    def delete(self, name):
        print(name)
        ad = FaceBookAds('test')
        d_ad = ad.delete_data(name)
        print(d_ad)
        return jsonify(d_ad)
