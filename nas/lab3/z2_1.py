#Пример 9.
m = float(input("Введите массу первого пакета в кг: "))
n = float(input("Введите массу второго пакета в кг: "))

# Сравниваем массу пакетов
if m > n:
    print("Первый пакет тяжелее второго.")
elif m < n:
    print("Второй пакет тяжелее первого.")
else:
    print("Масса обоих пакетов одинакова.")