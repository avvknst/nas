text = input("Введите строку: ")

# Подсчет количества букв "r" и "t"
count_r = text.count('r') + text.count('R')
count_t = text.count('t') + text.count('T')

print("Количество букв 'r' в строке:", count_r)
print("Количество букв 't' в строке:", count_t)