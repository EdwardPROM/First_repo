# def plus(a, b):
#   return a + b

# a = int (input("Веди число любое:"))
# b = int (input("Веди число любое:"))
# res = plus(a, b)
# print(res)  # Виведе 7

x = 50

def func():
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('x як і раніше', x)   # x як і раніше 50