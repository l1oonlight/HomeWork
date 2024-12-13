import re

text = input()
if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text):
    print('private')
elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', text):
    print('taxi')
else:
    print('Error_404')