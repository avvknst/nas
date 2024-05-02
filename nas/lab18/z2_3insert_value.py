# insert_value.py

def insert_value_into_sorted_list(sorted_list, value):
    index = 0
    while index < len(sorted_list) and sorted_list[index] < value:
        index += 1
    sorted_list.insert(index, value)
    return sorted_list
