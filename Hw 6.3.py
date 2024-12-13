def is_magic_square(matrix):
    n = len(matrix)  # Размер матрицы (n x n)
    
    # Сумма первой строки как эталон
    target_sum = sum(matrix[0])
    
    # Проверка сумм строк
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Проверка сумм столбцов
    for col in range(n):
        column_sum = sum(matrix[row][col] for row in range(n))
        if column_sum != target_sum:
            return False
    
    # Проверка главной диагонали
    diagonal_sum = sum(matrix[i][i] for i in range(n))
    if diagonal_sum != target_sum:
        return False
    
    # Проверка побочной диагонали
    anti_diagonal_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if anti_diagonal_sum != target_sum:
        return False
    
    return True

# Ввод матрицы с клавиатуры
def input_matrix(n):
    matrix = []
    print(f"Введите элементы матрицы {n}x{n}:")
    for i in range(n):
        row = list(map(int, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
        matrix.append(row)
    return matrix

# Пример использования
n = int(input("Введите порядок матрицы (n): "))
matrix = input_matrix(n)

# Проверка, является ли матрица магическим квадратом
if is_magic_square(matrix):
    print("Это магический квадрат.")
else:
    print("Это не магический квадрат.")
