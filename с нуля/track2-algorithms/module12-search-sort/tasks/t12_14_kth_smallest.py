"""
Задача 12-14. K-й по величине

Напишите функцию kth_smallest(items, k), которая возвращает k-й наименьший
элемент списка (k от 1). Список целиком не сортируйте и sorted не вызывайте:
k раз извлекайте минимум из копии списка.

Примеры
--------
kth_smallest([7, 1, 5, 3], 2)  → 3
kth_smallest([9, 2], 1)        → 2
"""


def kth_smallest(items, k):
    if k < 1 or k > len(items):
        raise ValueError("k is out of bounds")

    items_copy = items.copy()
    for _ in range(k - 1):
        min_value = min(items_copy)
        items_copy.remove(min_value)

    return min(items_copy)
