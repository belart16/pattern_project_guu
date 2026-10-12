"""
Задача 12-13. Убрать повторы за один проход

Напишите функцию dedupe_sorted(items), которая принимает отсортированный
список и возвращает список без повторов — за один проход, сравнивая
соседние элементы (множества не использовать: их результат теряет порядок
и требует сортировки).

Примеры
--------
dedupe_sorted([1, 1, 2, 3, 3, 3]) → [1, 2, 3]
"""


def dedupe_sorted(items):
    if not items:
        return []

    deduped = [items[0]]

    for i in range(1, len(items)):
        if items[i] != items[i - 1]:
            deduped.append(items[i])

    return deduped
