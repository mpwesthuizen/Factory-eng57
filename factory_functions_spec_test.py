# Define the tests before we code the functions
from factory_functions import *

# <user story> As a user, I want to make dough with water and flour, so that I can then make bread (3)
# test 1
print("When make_dough is called with 'water' and 'flour' it should return 'dough'")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

# test 2 - make_dough()
print("When make_dough is called with 'water' and 'cement' it should return ' not dough'")
print(make_dough('water', 'cement') == 'not dough')

#<user story> As a user, I want to bake bread with dough, so that I can the sell it (3)
# test 1
print("When bake_bread is called with dough return bread")
print(make_bread('dough') == 'bread')
print('got:', make_bread('dough'))

# test 2 - bake_bread()
print("When bake_bread is called with not dough return not bread")
print(make_bread('not dough') == 'not bread')
print('got:', make_bread('not dough'))

#<user story> As a user, I want to bake wholewheat bread with wholewheat dough, so that I can then sell it to my niche clients(3)
# test 1
print("When make_ww_dough is called with 'water' and 'wholewheat flour' it should return 'wholewheat dough'")
print(make_ww_dough('water', 'wholewheat flour') == 'wholewheat dough')
print('got:', make_ww_dough('water', 'wholewheat flour'))

# test 2 - make_wholewheat_dough()
print("When make_dough is called with 'water' and 'glass shards' it should return ' not wholewheat dough'")
print(make_ww_dough('water', 'glass shards') == 'not wholewheat dough')
print('got:', make_ww_dough('water', 'wholewheat flour'))

#<user_story> As a user, I want to make wholewheat bread when given wholewheat flour and water, so that I can use the factory downtime more effectively and try new markets.(3)
# test 1
print("When bake_bread is called with whole wheat dough return wholewheat bread ")
print(bake_ww_bread('wholewheat dough') == 'wholewheat bread')
print('got:', bake_ww_bread(' wholewheat dough'))

# test 2
print("When bake_ww_bread is called with not wholewheat dough return not wholewheat bread")
print(bake_ww_bread('not dough') == 'not wholewheat bread')
print('got:', bake_ww_bread('not dough'))
