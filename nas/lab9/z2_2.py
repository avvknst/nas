words = input("Введите строку слов, разделенных пробелами: ")

# Разбиение строки на слова
word_list = words.split()

# Нахождение самого длинного слова
max_length_word = max(word_list, key=len)

print("Самое длинное слово:", max_length_word)