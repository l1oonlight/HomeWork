import re

text = input()
print(len(re.findall(r'\b\w[\w-]*\b', text)))