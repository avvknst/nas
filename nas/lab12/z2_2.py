n = int(input("Введите размерность квадратной матрицы: "))
matrix = [[int(input(f"Элемент [{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]

# Замена отрицательных элементов матрицы на нули
for i in range(n):
    for j in range(n):
        if matrix[i][j] < 0:
            matrix[i][j] = 0

# Вывод результата
print("Матрица после замены отрицательных элементов на нули:")
for row in matrix:
    print(row)