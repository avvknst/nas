import my_modulez1

print(my_modulez1.greet("Настя"))
print(my_modulez1.calculate_sum(5, 3))

number = 17
if my_modulez1.is_prime(number):
    print(f"{number} - простое число.")
else:
    print(f"{number} - не является простым числом.")
