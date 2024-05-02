# max_digit_sum.py

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def find_max_digit_sum(numbers):
    max_sum = 0
    max_num = None
    for num in numbers:
        current_sum = digit_sum(num)
        if current_sum > max_sum:
            max_sum = current_sum
            max_num = num
    return max_num
