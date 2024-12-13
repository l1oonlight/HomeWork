#Формула T = 2π√(L/g)
#Условия : точность до сотых
#g = 9.81

from math import *

L, g = int(input()), 9.81
print(f'Период колебаний равен : {round(2 * pi * sqrt(L/g), 2)}')