def print_average(numbers):
    if not numbers:
        print("0")
    else:
        average = sum(numbers) / len(numbers)
        print("Среднее значение:", average)

# Ввод списка с клавиатуры
numbers = list(map(int, input("Введите список целых чисел, разделенных пробелами: ").split()))

# Вызов функции
print_average(numbers)