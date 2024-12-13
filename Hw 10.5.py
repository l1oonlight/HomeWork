import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 29, 34]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'grade': ['A', 'B', 'C']
})

df_merged = pd.merge(df1, df2, on='id')

print("Объединенный DataFrame:")
print(df_merged)

grade_map = {'A': 4, 'B': 3, 'C': 2}
df_merged['grade_numeric'] = df_merged['grade'].map(grade_map)

plt.figure(figsize=(8, 6))
plt.plot(df_merged['grade_numeric'], df_merged['age'], label='Age vs Grade', marker='o')

plt.title("Зависимость возраста от оценки")
plt.xlabel("Оценка (числовое значение)")
plt.ylabel("Возраст")
plt.legend()

plt.grid(True)
plt.show()