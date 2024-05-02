# main_program.py

import z3max_digit_sum

N = [123, 456, 789, 1111, 2222]  # Список целых чисел

print(f"Исходные числа: {N}")

max_num = z3max_digit_sum.find_max_digit_sum(N)

print(f"Число с максимальной суммой цифр: {max_num}")
