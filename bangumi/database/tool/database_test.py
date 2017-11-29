import copy

import arrow
from mongoengine import connect
from mongoengine.context_managers import switch_collection

from bangumi.database.animate import Animate
from bangumi.database.person import Person


def show_animate():
    connect('animate_data', host='mongodb://localhost/acg')
    for animate in Animate.objects:
        print(animate['name'])


def show_birth():
    connect('animate_data', host='mongodb://localhost/acg')
    for person in Person.objects():
        try:
            print(person.info['生日: '])
            print(person.japan_name)
        except:
            pass


def copy_collection():
    connect('animate_data', host='mongodb://localhost/acg')
    for animate in Animate.objects:
        with switch_collection(Animate, 'copy_animate') as copy_animate:
            copy_animate = copy.deepcopy(animate)
            copy_animate.id = None
            copy_animate.save()
    print('ok!')


def get_info_dict_key():
    connect('animate_data', host='mongodb://localhost/acg')
    field_dict = dict()
    for animate in Animate.objects:

        try:
            raw_time = animate.info['放送开始'][0]
            print(raw_time)
            time = arrow.get(raw_time, 'YYYY年M月D日')
            time = time.datetime
            print('from %s , to %s' % (raw_time, time))

        except:
            pass


if __name__ == '__main__':
    get_info_dict_key()
