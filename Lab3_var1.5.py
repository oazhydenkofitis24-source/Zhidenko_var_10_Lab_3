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
a = int(input("Введіть число: "))
n = int(input("Введіть степінь: "))
print(power(a, n))

input()
