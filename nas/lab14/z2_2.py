n = int(input("Введите количество сотрудников: "))
vacations = {}
for i in range(n):
    vacation_info = input().split()
    vacations[vacation_info[0]] = vacation_info[1:]

# Запрос
month = input("Введите название месяца: ")

# Вывод
if month in [vacation[1] for vacation in vacations.values()]:
    print(*[employee for employee, vacation in vacations.items() if vacation[1] == month], sep=' ')
else:
    print()