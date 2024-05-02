def sum_expression(n):
    total_sum = 0
    for k in range(1, n + 1):
        for m in range(1, n + 1):
            total_sum += n / (2 * k + m)
    return total_sum

n = 5
result = sum_expression(n)
print(f"Сумма для n = {n} равна: {result}")