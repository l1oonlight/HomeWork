def longest_words(file):
    f = open(file, 'r', encoding='utf-8')
    lines = f.readlines()
    long = set()
    for i in lines:
        arigato = i.split()
        long.add(max(arigato, key=len))
    if len(long) > 0: return max(long, key=len)

print(longest_words('C:/Users/Moonlight/Desktop/article.txt'))