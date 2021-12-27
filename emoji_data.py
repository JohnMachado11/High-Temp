import emoji
from city_data import city_country_flags


emojis_dictionary = {
    "fire": ":fire:",
    "point_up": ":backhand_index_pointing_up:",
    "cityscape": ":cityscape:",
    "randomize": ":dizzy:",
    "grinning_face": ":grinning_face_with_big_eyes:",
    "expressionless_face": ":expressionless_face:",
    "victory_hand": ":victory_hand:",
    "check_mark": ":check_mark_button:"
}


def emoji_maker(*args):
    
    if args:
        player_flag = emoji.emojize(city_country_flags[args[0]])
        player2_flag = emoji.emojize(city_country_flags[args[1]]) 

        return player_flag, player2_flag
    else:
        fire = emoji.emojize(emojis_dictionary['fire'])
        point_up = emoji.emojize(emojis_dictionary['point_up'])
        cityscape = emoji.emojize(emojis_dictionary['cityscape'])
        randomize = emoji.emojize(emojis_dictionary['randomize'])
        grinning_face = emoji.emojize(emojis_dictionary['grinning_face'])
        expressionless_face = emoji.emojize(emojis_dictionary['expressionless_face'])
        victory_hand = emoji.emojize(emojis_dictionary['victory_hand'])
        check_mark = emoji.emojize(emojis_dictionary['check_mark'])

        return fire, point_up, cityscape, randomize, grinning_face, expressionless_face, victory_hand, check_mark
