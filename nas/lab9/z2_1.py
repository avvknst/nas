string = input("Введите строку: ")

# Повторение каждого символа строки дважды
doubled_string = ''.join([char * 2 for char in string])

print("Строка с удвоенными символами:", doubled_string)