# Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке
# нечетные числа в порядке возрастания их индексов, а также их количество K.

import random

try:
    numbers = [random.randint(1, 100) for _ in range(10)]
    print("Исходный список:", numbers)

    K = 0

    print("Нечетные числа в порядке возрастания индексов:")
    for number in numbers:
        if number % 2:
            print(number)
            K += 1

    print(f"Количество нечетных чисел: {K}")
except ValueError:
    print("Внимание произошла ошибка")