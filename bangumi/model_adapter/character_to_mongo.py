from bangumi.database.character import Character, CharacterPlay
from bangumi.model_adapter.base_adapter import item_to_document


def character_to_mongo(item):
    character = Character()
    for character_attr in item:
        if character_attr == 'play':
            character.play = list()
            for play in item['play']:
                character_player = CharacterPlay()
                character_player = item_to_document(character_player, play)
                character.play.append(character_player)
            continue
        setattr(character, character_attr, item[character_attr])

    return character
