sequence = input("Введите последовательность символов: ")

char_set = set()

# Добавление цифр от '5' до '9' и знаков арифметических операций в множество
for char in sequence:
    if char.isdigit():
        if char >= '5' and char <= '9':
            char_set.add(char)
    elif char in ['+', '-', '*', '/']:
        char_set.add(char)

print("Множество цифр и знаков арифметических операций:", char_set)