numbers = [int(input(f"Введите число {i+1}: ")) for i in range(10)]

# Находим индекс наименьшего элемента
min_index = numbers.index(min(numbers))

# Меняем местами последний элемент и элемент с наименьшим значением
numbers[-1], numbers[min_index] = numbers[min_index], numbers[-1]

# Вывод результата
print("Список после замены наименьшего элемента с последним:", numbers)