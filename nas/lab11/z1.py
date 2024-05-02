num_grades = int(input("Введите количество оценок: "))

# Инициализация списка оценок
grades = []

# Ввод оценок и добавление их в список
print("Введите оценки:")
for i in range(num_grades):
    grade = float(input())
    grades.append(grade)

# Вывод оценок в том же порядке
print("Введенные оценки:")
for grade in grades:
    print(grade)

# Вычисление средней оценки
average_grade = sum(grades) / num_grades
print("Средняя оценка за урок:", average_grade)