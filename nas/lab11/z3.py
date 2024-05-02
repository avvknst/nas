import random

# Создание списка из 20 случайных целых чисел в диапазоне [-100, 100]
numbers = [random.randint(-100, 100) for _ in range(20)]

# Вывод исходного списка
print("Исходный список:")
print(numbers)

# Нахождение наибольшего элемента в списке
max_index = numbers.index(max(numbers))

# Обмен наибольшего элемента с первым элементом списка
numbers[0], numbers[max_index] = numbers[max_index], numbers[0]

print("\nСписок после замены:")
print(numbers)