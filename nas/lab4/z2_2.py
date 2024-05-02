import math

# Ввод данных
a = 2.6
b = -0.39
x = float(input("Введите значение x: "))

# Вычисление значения функции
if x < 2.8:
    y = x * ((x - a) ** (1 / 3))
elif 2.8 <= x < 6:
    y = (a + b) / (x + 1)
else:
    y = math.e ** x + math.sin(x)

# Вывод результата
print("Значение функции y =", y)