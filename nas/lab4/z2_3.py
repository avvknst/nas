import math

# Ввод данных
a = 2.5
b = 0.4

t = float(input("Введите значение x: "))

# Вычисление значения функции
if t < 0.1:
    y = math.sqrt(a * t ** 2 + b * math.sin(t) + 1)
elif t == 0.1:
    y = a * t + b
else:
    y = math.sqrt(a * t ** 2 + b * math.cos(t) + 1)

# Вывод результата
print("Значение функции y =", y)