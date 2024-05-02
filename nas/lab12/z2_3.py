n = int(input("Введите размерность квадратной матрицы: "))
matrix = [[int(input(f"Элемент [{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]

# Ввод значения k
k = int(input("Введите значение k: "))

# Подсчет числа элементов, кратных k
count = sum(1 for i in range(n) for j in range(n) if matrix[i][j] % k == 0)

# Вывод результата
print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"Число элементов, кратных {k}: {count}")