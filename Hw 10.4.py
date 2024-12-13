import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 21, 22]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'grade': ['A', 'B', 'C']
})

df_vertical = pd.concat([df1, df2], ignore_index=True)

print("Вертикальная конкатенация:")
print(df_vertical)