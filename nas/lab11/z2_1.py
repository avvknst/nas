# Ввод списка В
B = [int(input(f"Введите элемент {i+1}: ")) for i in range(20)]

# Вычисление суммы положительных элементов
positive_sum = sum(num for num in B if num > 0)

# Вывод результата
print("Сумма положительных элементов в списке B:", positive_sum)