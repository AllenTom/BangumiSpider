import pymongo
from mongoengine import connect

from .randomproxy import RandomProxy

connect('animate_data', host='mongodb://localhost/bangumi')
connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection['bangumi']

from logbook import Logger, StreamHandler
import sys

StreamHandler(sys.stdout).push_application()
