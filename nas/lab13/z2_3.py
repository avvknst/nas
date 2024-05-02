string = input("Введите строку, состоящую из нескольких слов, разделенных пробелами: ")

# Преобразование строки
transformed_string = ":".join(sorted("".join(string.split())))

print("Результат:", transformed_string)