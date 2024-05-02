Y = [int(input(f"Введите элемент {i+1}: ")) for i in range(15)]

# Нахождение наименьшего элемента и его порядкового номера
min_value = min(Y)
min_index = Y.index(min_value)

# Вывод результата
print("Наименьший элемент:", min_value)
print("Его порядковый номер:", min_index + 1)