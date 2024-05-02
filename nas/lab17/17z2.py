import random

def generate_schedule(num_exams, subjects):
    days_of_week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
    times = list(range(9, 15))
    tickets = list(range(1, 21))

    for _ in range(num_exams):
        subject = subjects.pop(random.randint(0, len(subjects)-1))
        day = random.choice(days_of_week)
        exam_time = random.choice(times)
        times.remove(exam_time)
        ticket_number = random.choice(tickets)

        print(f"Экзамен по дисциплине «{subject}» состоится в {day} время {exam_time}. Ваш счастливый билет N {ticket_number}.")

num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименования дисциплин через запятую и пробел: ").split(', ')

generate_schedule(num_exams, subjects)
