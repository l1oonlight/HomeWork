import re
string = input().lower()
nnn = re.findall('[н]+',string)
nnn_len = map(len,nnn)
maximal_nnn = max(nnn_len)
string_replaced = string.replace('н','!')
print(string_replaced)
print(maximal_nnn)