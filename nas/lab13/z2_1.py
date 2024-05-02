sentence = input("Введите строку с несколькими словами: ")

# Преобразование строки: каждое слово в верхний регистр и добавление дефисов
transformed_sentence = '-'.join(word.upper() for word in sentence.split())

# Вывод преобразованной строки
print("Преобразованная строка:", transformed_sentence)