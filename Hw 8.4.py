import re

def extract_abbreviations(text):
    words = text.split()
    
    abbreviations = []
    current_abbreviation = []

    for word in words:
        if re.match(r'^[А-ЯA-Z]{2,}$', word):
            current_abbreviation.append(word)
        else:
            if current_abbreviation:
                abbreviations.append(" ".join(current_abbreviation))
                current_abbreviation = []
    
    if current_abbreviation:
        abbreviations.append(" ".join(current_abbreviation))

    return abbreviations

text = "Ты поступил в ЦНИЛЧХРЛЪ ? Нет. Я поступил в СПБПУ"
abbreviations = extract_abbreviations(text)

# Выводим результат
print("Найденные аббревиатуры:")
for abbreviation in abbreviations:
    print(abbreviation)