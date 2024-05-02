n = 40
sum_of_squares = 0
for i in range(1, 2*n+1, 2):
    sum_of_squares += i**2
print("Сумма квадратов первых", n, "нечетных чисел:", sum_of_squares)