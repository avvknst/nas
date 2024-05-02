M = int(input("Введите количество строк матрицы: "))
N = int(input("Введите количество столбцов матрицы: "))

# Ввод элементов матрицы
matrix = []
print("Введите элементы матрицы:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вывод элементов матрицы в заданном порядке
for i in range(M):
    if i % 2 == 0:
        print(*matrix[i])
    else:
        print(*matrix[i][::-1])