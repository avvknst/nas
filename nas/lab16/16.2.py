# Заданный список
numbers = [12, 49, 34, 51, 68, 85, 102, 136, 153, 170]

# Извлечение чисел, делимых на 17
result = [number for number in numbers if number % 17 == 0]

# Печать результатов
print("Числа из списка, делимые на 17:")
for number in result:
    print(number)
