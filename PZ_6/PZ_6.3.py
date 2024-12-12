#  Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть
# числа, меньшие своих соседей).

import random
def local_minima(lst):
    try:
        for i in range(len(lst)):
            if (i == 0 or lst[i] < lst[i - 1]) and (i == len(lst) - 1 or lst[i] < lst[i + 1]):
                lst[i] **= 2
    except IndexError:
        print("Ошибка: индекс вышел за пределы списка.")
    except TypeError:
        print("Ошибка: список содержит некорректные данные.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return lst


try:
    N = int(input("Введите размер списка (целое число больше 0): "))
    if N <= 0:
        print("Размер списка должен быть больше 0.")
        exit()
except ValueError:
    print("Ошибка: введено некорректное значение. Пожалуйста, введите целое число.")
    exit()


lst = [random.randint(1, 100) for _ in range(N)]
print("Исходный случайный список:", lst)

result = local_minima(lst)
print("Список после возведения локальных минимумов в квадрат:", result)