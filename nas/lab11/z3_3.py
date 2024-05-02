numbers = [float(input(f"Введите число {i+1}: ")) for i in range(12)]

# Разделение списка на отрицательные и положительные числа
negative_numbers = [num for num in numbers if num < 0]
positive_numbers = [num for num in numbers if num >= 0]

# Объединение списков с сохранением порядка
numbers = negative_numbers + positive_numbers

print("Список после разделения на отрицательные и положительные числа:", numbers)