def find_max_values(matrix):
    max_in_third_column = max(matrix[i][2] for i in range(3))
    max_in_second_row = max(matrix[1])
    print(f"Максимальное значение среди элементов третьего столбца: {max_in_third_column}")
    print(f"Максимальное значение среди элементов второй строки: {max_in_second_row}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

find_max_values(matrix)