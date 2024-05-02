n = int(input("Введите количество специальностей: "))
specialties = {}
for i in range(n):
    specialty_info = input().split('-')
    specialty = specialty_info[0]
    groups = specialty_info[1].split(',')
    specialties[specialty] = groups

# Запрос
group = input("Введите номер группы: ")

# Вывод
for specialty, groups in specialties.items():
    if group in groups:
        print(specialty)
        break
else:
    print()