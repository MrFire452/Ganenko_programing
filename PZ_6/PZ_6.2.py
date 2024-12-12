# Дан список размера N. Найти минимальный из его локальных максимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).
import random

def min_local_maximum(lst):
    local_maxima = []

    try:
        for i in range(len(lst)):
            if (i == 0 or lst[i] > lst[i - 1]) and (i == len(lst) - 1 or lst[i] > lst[i + 1]):
                local_maxima.append(lst[i])
    except IndexError:
        print("Ошибка: индекс вышел за пределы списка.")
        return None
    except TypeError:
        print("Ошибка: список содержит некорректные данные.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

    if not local_maxima:
        print("В списке нет локальных максимумов.")
        return None

    return min(local_maxima)

try:
    N = int(input("Введите размер списка (целое число больше 0): "))
    if N <= 0:
        print("Размер списка должен быть больше 0.")
        exit()
except ValueError:
    print("Ошибка: введено некорректное значение. Пожалуйста, введите целое число.")
    exit()

lst = [random.randint(1, 100) for _ in range(N)]
print("Случайный список:", lst)

result = min_local_maximum(lst)
if result is not None:
    print(f"Минимальный локальный максимум: {result}")