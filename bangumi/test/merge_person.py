import pymongo
from mongoengine import connect

from bangumi.database.person import Person


def merge_person():
    connect('animate_data', host='mongodb://localhost/acg')
    person_list = Person.objects
    for person in person_list:
        person_find = Person.objects(bangumi_id=person.bangumi_id)
        if len(person_find) > 1:
            for i in range(1, len(person_find)):
                person_find[i].delete()
                print('delete %s' % person_find.id)


if __name__ == '__main__':
    connection = pymongo.MongoClient('127.0.0.1', 27017)
    db = connection['reACG']
    collection = db['person']
    print(collection.find_one({'bangumi_id': '9356'}))

