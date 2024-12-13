from random import randint
m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(m):
    brr = list()
    for j in range(n):
        brr.append(randint(-10, 10))
    arr.append(brr)
print(arr)
summi = {}
for i in arr:
    summi.update({sum(i):i})
print(f'максимальная сумма {max(summi.keys())} у строчки {summi.get(max(summi.keys()))}')
print(f'минимальная сумма {min(summi.keys())} у строчки {summi.get(min(summi.keys()))}')