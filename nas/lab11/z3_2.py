numbers = [float(input(f"Введите число {i+1}: ")) for i in range(10)]

# Сортировка списка по убыванию
numbers.sort(reverse=True)

print("Список после сортировки по убыванию:", numbers)