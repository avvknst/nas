set1 = set(map(int, input("Введите элементы первого множества через пробел: ").split()))
set2 = set(map(int, input("Введите элементы второго множества через пробел: ").split()))


unique_numbers = set1.union(set2)

common_numbers = sorted(set1.intersection(set2))

print("Все различные числа в двух множествах:", unique_numbers)
print("Числа, которые входят как в первое, так и во второе множества (в порядке возрастания):", common_numbers)