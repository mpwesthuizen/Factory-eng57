# Define the tests before we code the functions
from Factory_functions import *

# test 1
print("When make_dough is called with 'water' and 'flour' it should return 'dough'")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

# test 2 - make_dough()
print("When make_dough is called with 'water' and 'cement' it should return ' not dough'")
print(make_dough('water', 'cement') == 'not dough')