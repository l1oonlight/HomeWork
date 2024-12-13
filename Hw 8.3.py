import re

text = input()
for i in re.findall(r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)', text):
     text = text.replace(i, '(TBD)')
print(text)
ext = input()
print(re.findall(r'(?:[АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ]{2,}[ ]*)+', text))