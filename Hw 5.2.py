def palindrom(n):
    newn = bin(n)[2:]
    if newn == newn[::-1]:
        return newn
    else:
        return ''


n = int(input())
rez = {}
for i in range(n + 1):
    if palindrom(i) != '':
        rez.update({i: palindrom(i)})
print(f'Числа-палиндромы : {rez}')