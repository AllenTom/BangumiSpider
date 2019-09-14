import os

import pymongo

from .randomproxy import RandomProxy


def get_connection_string():
    username = os.environ['MONGO_USERNAME'] if 'MONGO_USERNAME' in os.environ else "admin"
    password = os.environ['MONGO_PASSWORD'] if 'MONGO_PASSWORD' in os.environ else "admin"
    host = os.environ['MONGO_HOST'] if 'MONGO_HOST' in os.environ else "127.0.0.1"
    port = os.environ['MONGO_PORT'] if 'MONGO_PORT' in os.environ else "27017"
    return f"mongodb://{username}:{password}@{host}:{port}"


connection = pymongo.MongoClient(get_connection_string())
db = connection['bangumi']

from logbook import StreamHandler
import sys

StreamHandler(sys.stdout).push_application()
