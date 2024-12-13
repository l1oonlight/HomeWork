def transform_array(matrix):
    # Создаем новый массив, заменяя элементы по условию
    new_matrix = [[1 if matrix[i][j] > 0 else (0 if matrix[i][j] < 0 else matrix[i][j]) 
                   for j in range(len(matrix[i]))] for i in range(len(matrix))]
    
    print("Исходный массив:")
    for row in matrix:
        print(row)
    
    print("\nНовый массив:")
    for row in new_matrix:
        print(row)

n, m = int(input('Введите кол-во строк матрицы : ')), int(input('Введите кол-во столбцов матрицы : '))
matrix = []
for i in range(n):
    matrix += [[int(input("Введите значения : ")) for _ in range(m)]]

for line in matrix:
    print(*line)

# Вызов функции
transform_array(matrix)