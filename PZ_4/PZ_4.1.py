#  Даны два целых числа A и B (A < Б). Найти произведение всех целых чисел от A до B включительно.

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

itog = 1

for number in range(A, B + 1):
    itog *= number

print(f"Произведение всех целых чисел от A до B: {itog}")