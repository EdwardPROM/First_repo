def split_list(grade):
    if not grade:
        return [], []
    average = sum(grade) / len(grade)
    greater_than_average = []  # Список для чисел більших за середнє значення
    less_than_average = []  # Список для чисел менших за середнє значення
    
    for num in grade:
        if num <= average:
            less_than_average.append(num)
        elif num >= average:
            greater_than_average.append(num)

    return less_than_average, greater_than_average


a = split_list ([])
print (a)

# У нас є список показників студентів групи – це список з отриманими балами з тестування. 
# Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), 
# знаходить середнє значення бала у списку та ділить його на два списки. 
# У перший потрапляють значення менше середнього, включаючи середнє значення, 
# тоді як у другий — строго більше від середнього. Функція повертає кортеж цих двох списків. 
# Для порожнього списку повертаємо два порожні списки.