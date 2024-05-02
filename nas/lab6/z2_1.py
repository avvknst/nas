import math

k = int(input("Введите число k: "))

# Вывод корня и куба для чисел от 0 до k
for i in range(k+1):
    square_root = math.sqrt(i)
    cube = i ** 3
    print(f"Корень числа {i} равен {square_root}, а куб равен {cube}")