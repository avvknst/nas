def count_spaces(string):
    space_count = string.count(' ')
    if space_count % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")

# Ввод строки с клавиатуры
string = input("Введите строку: ")

# Вызов функции
count_spaces(string)