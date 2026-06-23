def power(a, n):
    # Базовий випадок
    if n == 0:
        return 1
    # Додатній степінь
    elif n > 0:
        return a * power(a, n - 1)
    # Від’ємний степінь
    else:
        return 1 / power(a, -n)

# Приклади використання
print(power(2, 3))   # 8
print(power(2, -3))  # 0.125
print(power(5, 0))   # 1