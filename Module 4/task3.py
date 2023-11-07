# def format_ingredients(items):
#     items = []
#     for i in items:
#         print (i)
     
        
# a = format_ingredients (["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"])
# print (a)        
    
# my_list = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]

# # Вывести список без кавычек с помощью метода join()
# print(", ".join(my_list))    
        
    
    
# Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, 
# а перед останнім ставимо союз "and", як у прикладі нижче:

# 2 eggs, 1 liter sugar, 1 tsp salt and vinegar
# Напишіть функцію format_ingredients, яка прийматиме на вхід список 
# з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок зібраний з його елементів в описаний вище спосіб. 
# Ваша функція має вміти обробляти списки будь-якої довжини.  
def format_ingredients(ingredients):
    if len(ingredients) == 0:
        return ""
    elif len(ingredients) == 1:
        return ingredients[0]
    else:
        # Використовуємо коми для розділення всіх інгредієнтів, крім останнього
        formatted = ", ".join(ingredients[:-1])
        # Додаємо "and" та останній інгредієнт
        formatted += f" and {ingredients[-1]}"
        return formatted

