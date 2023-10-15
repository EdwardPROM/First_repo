def fibonacci(n):
    """
    Рекурсивно обчислює число Фібоначчі за його порядковим номером.

    Args:
      n: Порядковий номер числа Фібоначчі.

    Returns:
      Значення числа Фібоначчі.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)