numbers = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
start, end = map(int, input("Введите начальный и конечный номера интервала (через пробел): ").split())

# Вычисление произведения чисел в интервале
product_of_interval = 1
for number in numbers[start:end+1]:
    product_of_interval *= number

print("Произведение чисел в интервале:", product_of_interval)
