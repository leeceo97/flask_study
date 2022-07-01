from bson import json_util
from pymongo import MongoClient, ReturnDocument
import datetime
from flask import current_app, json, jsonify

client = MongoClient('127.0.0.1', 27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client.my_database
# db = client['my_database']

# 콜렉션 이름 지정
ads_collection = db.test
# collection = db[test]

class FaceBookAds:
    def __init__(self, db_name):
        self.col = client['my_database'][db_name]

    def _get_object(self):
        pass

    def find_all(self):
        db = self.col
        ads = db.find()
        response_data = []
        for ad in ads:
            response_data.append(ad)
        #json.loads(json_util.dumps(response_data))
        return response_data

    def insert_data(self, **data):
        db = self.col
        result = db.insert_one(data)
        return data

    def find_one(self, name):
        db = self.col
        ad = db.find_one({'name':name})
        return jsonify(ad)

    def update_data(self, name, update_name):
        db = self.col
        ad = db.find_one_and_update({'name': name}, {'$set': {'name': update_name}}, return_document=ReturnDocument.AFTER)
        print(ad)
        return ad

    def delete_data(self, name):
        eb = self.col
        ad = db.find_one_and_delete({'name': name})
        return ad

