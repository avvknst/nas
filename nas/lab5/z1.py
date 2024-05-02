print("Введите числа. Для завершения введите 0.")
while True:
    number = float(input("Введите число: "))
    if number == 0:
        break
    print("Обратное число:", 1 / number)