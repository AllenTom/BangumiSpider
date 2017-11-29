import pymongo

from bangumi.database.animate import Animate


connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection['reACG']
collection = db['person']
print(collection.find_one({'bangumi_id' : 195553}))
