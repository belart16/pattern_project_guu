"""
Задача 12-12. Сколько обменов сделает пузырёк

Напишите функцию swap_count(items), которая возвращает, сколько обменов
соседних элементов выполнит пузырьковая сортировка данного списка.
Это число инверсий: пар (i, j), где i < j, а items[i] > items[j].

Примеры
--------
swap_count([1, 2, 3]) → 0
swap_count([3, 2, 1]) → 3
swap_count([3, 1, 2]) → 2
"""


def swap_count(items):
    count = 0
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                count += 1
                items[j], items[j + 1] = items[j + 1], items[j]

    return count
