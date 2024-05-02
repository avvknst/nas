word_indexes = input("Введите номера слов через пробел: ").split()
words = input("Введите слова через пробел: ").split()

# Формирование нового предложения
new_sentence = ' '.join(words[int(index) - 1] for index in word_indexes if index.isdigit())

# Преобразование первой буквы нового предложения в заглавную
new_sentence = new_sentence.capitalize()

print("Новое предложение:", new_sentence)