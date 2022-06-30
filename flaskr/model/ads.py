from pymongo import MongoClient
import datetime
from flask import current_app

client = MongoClient('127.0.0.1', 27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client.my_database
# db = client['my_database']

# 콜렉션 이름 지정
ads_collection = db.test
# collection = db[test]

class FaceBookAds:
    def __init__(self):
        self.col = client['my_database']['test']

    def find_all(self):
        print(self.col.fi)
        return self.col.find()
#document1 = {"name": "홍길동",
#            "bio": "한국인입니다.",
#            "tags": ["#몽고디비", "#파이썬", "#플라스크"],
#            "date": datetime.datetime.utcnow(),}
#document2 = {"name": "영희",
#             "bio": "한국인입니다.",
#             "tags": ["#MongoDB", "#Python", "#Flask"],
#             "date": datetime.datetime.utcnow(),}

#document = [document1, document2]
#collection.insert_many(document)
#ads_collection.update_one({'name':'영희'},{'$set':{'name':'이형준'}})
#print(ads_collection.find({'name':'이형준'}))