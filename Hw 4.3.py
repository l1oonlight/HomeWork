s = input().split()
out = []
for word in s:
    if word.lower().startswith('а') and word.lower().endswith('я'):
        out.append(word)
print(out)