import pymongo
from mongoengine import connect

from .randomproxy import RandomProxy

connect('animate_data', host='mongodb://localhost/bangumi_spider')
connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection['bangumi_spider']