from datetime import datetime, timedelta

def exam_date(days_until_exam):
    current_date = datetime.now()
    exam_date = current_date + timedelta(days=days_until_exam)
    return exam_date.strftime("%d %B")

days_until_exam = int(input("Введите количество дней до экзамена: "))
exam_day_month = exam_date(days_until_exam)
print(f"Дата экзамена: {exam_day_month}")
