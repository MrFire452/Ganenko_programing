# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить
# функцией с параметрами. Значения n и m программа должна запрашивать.
def sum_of_range(n, m):
    return sum(range(n, m + 1))

try:
    n = int(input("Введите начальное число: "))
    m = int(input("Введите конечное число: "))

    if n > m:
        print("Ошибка данных: начальное число n должно быть меньше или равно конечному числу m.")
    else:
        result = sum_of_range(n, m)
        print(f"Сумма чисел от {n} до {m} равна: {result}")
except ValueError:
    print("Ошибка. Введены некоректные данные")