num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

# Проверяем делится ли первое число на второе
if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} делится нацело на {num2}.")
else:
    print(f"{num1} не делится нацело на {num2}.")