import numpy as np
# Функция для ввода элементов матрицы
def input_matrix(n, m):
    matrix = []
    for i in range(n):
        row = input(f"Введите {m} элементов для строки {i + 1}: ").split()
        if len(row) != m:
            print("Ошибка! Введите ровно", m, "элементов.")
            return None
        matrix.append(row)
    return matrix
# Функция для проверки наличия нелатинских символов
def has_non_latin_characters(input_string):
    return any(not c.isalpha() and c != ' ' for c in input_string)
# Функция для изменения матрицы
def process_matrix(matrix):
    new_matrix = np.array(matrix, dtype=int)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if new_matrix[i][j] < 0:
                new_matrix[i][j] = 0
    return new_matrix
# Функция main для управления задачей
def main():
    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))
    matrix = input_matrix(n, m)
    if matrix is None:
        return
    input_str = input("Введите строку символов: ")
    if has_non_latin_characters(input_str):
        new_matrix = process_matrix(matrix)
        print("Новая матрица с отрицательными значениями замененными на 0:")
        print(new_matrix)
    else:
        print("Исходная матрица:")
        print(np.array(matrix, dtype=int))
if __name__ == "__main__":
    main()