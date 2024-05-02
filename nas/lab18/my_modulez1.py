def greet(name):
    return f"Привет, {name}! Добро пожаловать в мой модуль."

def calculate_sum(a, b):
    return a + b

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
