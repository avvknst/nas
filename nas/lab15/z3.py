def process_lists(list1, list2):
    a, b, c = list2  
    sum_other_elements = 0  
    
    for element in list1:
        # Проверяем условие: элемент больше a, меньше b и делится на c без остатка
        if a < element < b and element % c == 0:
            print(element)  
        else:
            sum_other_elements += element  # Суммируем элементы, которые не удовлетют условиям
    
    print("Сумма остальных элементов:", sum_other_elements)

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [15, 50, 10]
process_lists(list1, list2)