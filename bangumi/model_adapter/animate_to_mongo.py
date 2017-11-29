from bangumi.database.animate import *


def animate_item_to_mongodb(item):
    animate = Animate(
        bangumi_id=item['bangumi_id'],
        name=item['name'],
        summary=item['summary'],
        info=item['info'],
        tag=item['tag'],
        start_play=item['start_play'],
        episode_count=item['episode_count'],
        chinese_name=item['chinese_name'],
        cast=[
            AnimateCast(
                bangumi_id=cast['bangumi_id'],
                chinese_name=cast['chinese_name'],
                japan_name=cast['japan_name'],
                job=cast['job']
            ) for cast in item['cast']
        ],

        character=[
            AnimateCharacter(
                bangumi_id=character['bangumi_id'],
                japan_name=character['japan_name'],
                chinese_name=character['chinese_name'],
                job=character['job'],
                info=character['info'],
                cv=[
                    CharacterVoice(
                        bangumi_id=cv['bangumi_id'],
                        japan_name=cv['japan_name'],
                        chinese_name=cv['chinese_name']
                    ) for cv in character['cv']
                ]

            ) for character in item['character']

        ],
    )
    animate.episode = dict()
    for category in item['episode']:
        animate.episode[category] = [
            AnimateEpisode(
                number=episode['number'],
                japan_name=episode['japan_name'],
                chinese_name=episode['chinese_name'],
                show_date=episode['show_date'],

            ) for episode in item['episode'][category]
        ]

    return animate
