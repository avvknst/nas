import math

# Ввод данных
a = 1.65
x = float(input("Введите значение x: "))

# Вычисление значения функции
if x < 1.4:
    y = math.pi * x ** 2 - 7 / x ** 2
elif x == 1.4:
    y = a * x ** 3 + 7 * math.sqrt(x)
else:
    y = math.log(x) + 7 * math.sqrt(abs(x + a))

# Вывод результата
print("Значение функции y =", y)