import datetime
import re

import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection['reACG']


def fix_cv_blood():
    collection = db['Person']
    cv_list = collection.find({"job": "声优"})
    for cv in cv_list:
        if 'blood' in cv and cv['blood'] == 'A型':
            cv['blood'] = 'A'
            update_to_database(cv, collection)
            print(cv)


def find_cv():
    collection = db['Person']
    cv_list = collection.find({"job": "声优"})
    month = [0] * 13
    print(month)
    for cv in cv_list:
        if 'birthday' in cv:
            month[cv['birthday'].month] += 1

    print(month)


# fix bangumi 5554
def fix_birthday():
    collection = db['Person']
    cv_list = collection.find({"job": "声优"})
    counter = 0
    for cv in cv_list:
        for info_key in cv['info']:
            if str(info_key).find('生') != -1 and str(info_key).find('日') != -1:
                cv['birthday'] = format_time(str(cv['info'][info_key][0]))
                update_to_database(cv, collection)



def update_to_database(model, collection):
    model['updated'] = datetime.datetime.now()
    collection.replace_one({'_id': model['_id']}, model, upsert=True)


def format_time(time_str):
    if len(re.findall('\?\?\?\?-(\d+)-(\d+)', time_str, re.S)) != 0:
        date_group = re.findall('\?\?\?\?-(\d+)-(\d+)', time_str, re.S)[0]
        try:
            return datetime.datetime(month=int(date_group[0]), day=int(date_group[1]), year=2099)
        except:
            return None
    elif len(re.findall('(\d+)月(\d+)日', time_str, re.S)) != 0:
        date_group = re.findall('(\d+)月(\d+)日', time_str, re.S)[0]
        try:
            return datetime.datetime(month=int(date_group[0]), day=int(date_group[1]), year=2099)
        except:
            return None
    elif len(re.findall('(\d+)-(\d+)-(\d+)', time_str, re.S)) != 0:
        date_group = re.findall('(\d+)-(\d+)-(\d+)', time_str, re.S)[0]
        try:
            return datetime.datetime(month=int(date_group[1]), day=int(date_group[2]), year=int(date_group[0]))
        except:
            return None
    elif len(re.findall('(\d+)-(\d+)', time_str, re.S)) != 0:
        date_group = re.findall('(\d+)-(\d+)', time_str, re.S)[0]
        try:
            return datetime.datetime(month=int(date_group[0]), day=int(date_group[1]), year=2099)
        except:
            return None
    elif len(re.findall('(\d+)\.(\d+)\.(\d+)', time_str, re.S)) != 0:
        date_group = re.findall('(\d+)\.(\d+)\.(\d+)', time_str, re.S)[0]
        try:
            return datetime.datetime(month=int(date_group[1]), day=int(date_group[2]), year=int(date_group[0]))
        except:
            return None
    elif len(re.findall('(\d+)/(\d+)/(\d+)', time_str, re.S)) != 0:
        date_group = re.findall('(\d+)/(\d+)/(\d+)', time_str, re.S)[0]
        try:
            return datetime.datetime(month=int(date_group[1]), day=int(date_group[2]), year=int(date_group[0]))
        except:
            return None


if __name__ == '__main__':
    fix_birthday()
