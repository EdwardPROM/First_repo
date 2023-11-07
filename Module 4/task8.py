# def game(terra, power):
    

def game(terra, power):
    for sublist in terra:
        for energy_value in sublist:
            if energy_value <= power:
                power -= energy_value
            else:
                break
    return power

def game(terra, power):
    for sublist in terra:
        for energy_value in sublist:
            if energy_value <= power:
                power += energy_value
            else:
                break
    return power

# Приклад використання:
my_lists = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
initial_power = 1
final_power = game(my_lists, initial_power)
print("Загальна енергія гравця після гри:", final_power)