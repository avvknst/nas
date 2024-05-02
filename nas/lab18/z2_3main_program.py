# main_program.py

import z2_3insert_value

A = [1, 3, 5, 7, 9]  # Упорядоченный список

print(f"Исходный упорядоченный список A: {A}")

K = 4  # Значение, которое нужно вставить

new_sorted_list = z2_3insert_value.insert_value_into_sorted_list(A, K)

print(f"Упорядоченный список A после вставки значения {K}: {new_sorted_list}")
