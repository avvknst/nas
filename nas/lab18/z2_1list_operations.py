# list_operations.py

def exclude_value(list_A, value_K):
    list_B = [x for x in list_A if x != value_K]
    return list_B
