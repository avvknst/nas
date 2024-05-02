text = input("Введите строку: ")

# Подсчет количества символов ":"
count_colon = text.count(":")

# Удаление символа ":"
text_without_colon = text.replace(":", "")

print("Количество удаленных символов:", count_colon)
print("Строка без символов ':' :", text_without_colon)