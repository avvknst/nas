sequence = input("Введите последовательность символов: ")

char_set = set()

# Добавление знаков препинания и букв от 'E' до 'N' в множество
for char in sequence:
    if char in [',', '.', ';', ':']:
        char_set.add(char)
    elif char.isalpha():
        if char >= 'E' and char <= 'N':
            char_set.add(char)

print("Множество знаков препинания и букв от 'E' до 'N':", char_set)