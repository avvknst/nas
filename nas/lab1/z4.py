import random

num = random.randint(100, 999)
digits = [int(digit) for digit in str(num)]
print(*digits, sep=", ")