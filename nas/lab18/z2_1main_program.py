# main_program.py

import z2_1list_operations

A = [1, 2, 3, 4, 5, 4, 6, 7]
K = 4

print(f"Исходный список A: {A}")
print(f"Заданное значение K: {K}")

B = z2_1list_operations.exclude_value(A, K)

print(f"Список B без элементов со значением K: {B}")
