word = input("Введите слово: ")

# Создание словаря
dictionary = {}
for letter in word:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

print(dictionary)