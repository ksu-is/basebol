import pybaseball
import requests
import lxml
import tqdm
import bs4
import github
import matplotlib
import attr

from pybaseball import statcast
from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher

input("enter the name of a braves player to see their stats:")

def name_formatter(full_name):
    result = full_name.split(' ')
    return result[1]+', ' + result[0]
#print(name_formatter('max fried'))

def get_braves_stats(full_name):
    formatted_name = name_formatter(full_name)
    return playerid_lookup(formatted_name)
#print(get_braves_stats('Max Fried'))

playerid_lookup('fried', 'max')
#print(playerid_lookup('fried', 'max'))

def get_mlbam(last,first):
    result = playerid_lookup(last,first)
    return result['key_mlbam']

result = get_mlbam('fried','max')
print(result)

print(type(result))

def get_columns(last,first):
    result = playerid_lookup(last,first)
    return result.columns
print(get_columns('fried', 'max'))

'''
Index(['name_last', 'name_first', 'key_mlbam', 'key_retro', 'key_bbref',
       'key_fangraphs', 'mlb_played_first', 'mlb_played_last'],
      dtype='object')
pitch_type   game_date release_speed release_pos_x release_pos_z   
'''
fried_stats = statcast_pitcher('2019-06-01', '2020-07-01', 608331)
fried_stats.head(2)
print(fried_stats.head(2))




