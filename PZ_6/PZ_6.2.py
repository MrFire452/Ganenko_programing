# Дан список размера N. Найти минимальный из его локальных максимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).
def find_min_local_minimum(lst):
    local_minima = []

    try:
        for i in range(len(lst)):
            # Проверяем, является ли текущий элемент локальным минимумом
            if (i == 0 or lst[i] < lst[i - 1]) and (i == len(lst) - 1 or lst[i] < lst[i + 1]):
                local_minima.append(lst[i])
    except IndexError:
        print("Ошибка: индекс вышел за пределы списка.")
        return None
    except TypeError:
        print("Ошибка: список содержит некорректные данные.")
        return None

    if not local_minima:
        print("В списке нет локальных минимумов.")
        return None

    return min(local_minima)


# Пример использования
lst = [10, 5, 7, 8, 3, 4, 2, 6, 9]
result = find_min_local_minimum(lst)
if result is not None:
    print(f"Минимальный локальный минимум: {result}")
