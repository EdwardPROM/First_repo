def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

# Приклад використання:
fibonacci_function = caching_fibonacci()

# Обчислення числа Фібоначчі для n = 5
result_5 = fibonacci_function(5)
print(f"Fibonacci(5): {result_5}")

# Обчислення числа Фібоначчі для n = 10
result_10 = fibonacci_function(10)
print(f"Fibonacci(10): {result_10}")
