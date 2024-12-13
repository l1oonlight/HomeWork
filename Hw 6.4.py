def is_symmetric(matrix):
    n = len(matrix)  # Размер матрицы (n x n)
    
    # Проверка симметричности относительно главной диагонали
    for i in range(n):
        for j in range(i + 1, n):  # Проходим только верхнюю часть матрицы
            if matrix[i][j] != matrix[j][i]:  # Если элементы не равны, матрица не симметрична
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

# Проверка, является ли матрица симметричной
if is_symmetric(matrix):
    print("Матрица симметрична относительно главной диагонали.")
else:
    print("Матрица не симметрична относительно главной диагонали.")
