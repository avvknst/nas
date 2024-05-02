sequence = input("Введите последовательность символов: ")

char_set = set()

# Добавление знаков арифметических операций и знаков препинания в множество
for char in sequence:
    if char in ['+', '-', '*', '/', ',', '.', ';', ':']:
        char_set.add(char)

print("Множество знаков арифметических операций и знаков препинания:", char_set)