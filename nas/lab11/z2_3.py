X = [float(input(f"Введите элемент {i+1}: ")) for i in range(14)]

# Нахождение номеров элементов, удовлетворяющих условию
indexes = [i+1 for i, num in enumerate(X) if 0 < num < 1]

# Вывод результата
print("Номера элементов, удовлетворяющих условию 0 < X(i) < 1:", indexes)