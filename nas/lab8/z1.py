sentence = input("Введите строку из слов, разделенных пробелами: ")

words = sentence.split()

reversed_sentence = ' '.join(words[::-1])

print("Переставленные слова в обратном порядке:")
print(reversed_sentence)