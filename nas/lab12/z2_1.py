M = int(input("Введите количество строк матрицы: "))
N = int(input("Введите количество столбцов матрицы: "))

# Ввод элементов матрицы
matrix = []
print("Введите элементы матрицы:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вычисление суммы элементов каждого столбца матрицы
column_sums = [sum(row[j] for row in matrix) for j in range(N)]

# Вывод сумм элементов каждого столбца матрицы
print("Суммы элементов каждого столбца матрицы:")
for j in range(N):
    print(f"Сумма элементов столбца {j + 1}: {column_sums[j]}")