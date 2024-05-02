n = 5  # Значение n

# Используем вложенные циклы для суммирования выражения
result = sum(i**2 - 2*j for i in range(n+1) for j in range(n+1))

print("Результат:", result)