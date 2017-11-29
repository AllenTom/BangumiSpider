from mongoengine import connect

from bangumi.database.animate import Animate


def show_animate():
    connect('animate_data', host='mongodb://localhost/acg')
    for animate in Animate.objects:
        print(animate['name'])


if __name__ == '__main__':
    show_animate()