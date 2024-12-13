#Условие : Предел не меньше 100
import math as mt
num = int(input())
cube = 0
if num > 0 and num < 100:
    for i in range(1, num + 1):
        cube += mt.pow(i, 3)
    print(cube)
else:
    print('Error : the wrong border')