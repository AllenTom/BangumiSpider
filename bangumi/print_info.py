def print_animate(animate):
    print("-------------------%s--------------------" % animate['bangumi_id'])
    print("动画名称 : %s" % animate['name'])
    print("简介\n  %s" % animate['summary'])
    print('---------------------------------动画信息------------------------------')
    # for info_item in animate['info']:
    #     print(info_item['title'])
    #     for value in info_item['values']:
    #         print(str(value))
    #     print('\n')
    print('---------------------------------制作组信息------------------------------')
    for cast in animate['casts']:
        # print(cast['bangumi_person_id'])
        print('日本名 : %s ' % cast['japan_name'])
        print('中文名 : %s ' % cast['chinese_name'])
        print('job')
        for job in cast['job']:
            print(job)
        print('\n')

    print('---------------------------------角色信息------------------------------')
    for character in animate['character']:
        print(character['job'])
        print("日文名 : %s" % character['japan_name'])
        print("中文名 : %s" % character['chinese_name'])
        print('\n')
        for info in character['info']:
            print(info['title'])
            print(info['value'])

        print('\n')
        for cv in character['cv']:
            print(cv['bangumi_id'])
            print(cv['japan_name'])
            print(cv['chinese_name'])


def print_character_voice(cv):
    print('--------------------------------------------%s-------------------------------' % cv['bangumi_id'])
    print('名称 : %s ' % cv['name'])
    print('简介')
    print(cv['detail'])
    print('--------------------------------------------基本信息-------------------------------')
    for info in cv['info']:
        print(info['title'])
        for value in info['value']:
            print(value)
        print('\n')
    print('--------------------------------------------出演角色-------------------------------')
    for character in cv['character']:
        print('ID : %s' % character['bangumi_id'])
        print('日文名 : %s' % character['japan_name'])
        print('中文名 : %s' % character['chinese_name'])
        for work in character['work']:
            print('ID : %s' % work['bangumi_id'])
            print(work['job'])
            print('日文名 : %s' % work['japan_name'])
            print('中文名 : %s' % work['chinese_name'])
            print('\n')
        print('\n')

    print('--------------------------------------------作品-------------------------------')
    for work_item in cv['works']:
        print('ID : %s' % work_item['bangumi_id'])
        print(work_item['name'])
        print(work_item['job'])
        print('\n')

