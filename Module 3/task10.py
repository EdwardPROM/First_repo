def factorial(n):
    if n < 2:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)  # Рекурсивний випадок
            
def number_of_groups(n, k):
    result = factorial (n) // (factorial(n-k) * factorial (k))
    return result

print (number_of_groups(50,7))
# def number_of_groups(n, k):
    