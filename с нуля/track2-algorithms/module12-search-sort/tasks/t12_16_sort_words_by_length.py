"""
Задача 12-16 ★. Слова по длине

Напишите функцию sort_words_by_length(words), которая возвращает слова,
отсортированные по возрастанию длины, а при равной длине — по алфавиту.
Используйте встроенный sorted с key=lambda.

Примеры
--------
sort_words_by_length(["б", "аа", "в"]) → ["б", "в", "аа"]
"""


def sort_words_by_length(words):
    return sorted(words, key=lambda word: (len(word), word))
