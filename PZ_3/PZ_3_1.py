## 1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и C».
try:
    A = int(input("Введите число A:"))
    B = int(input("Введите число B:"))
    C = int(input("Введите число C:"))

    if (A < B < C) or (C < B < A):
        print("Число B находится между числами A и C.")
    else:
        print("Число B не находится между числами A и C.")
except:
    print("Произошла ошибка, пожалуйста повторите попытку")