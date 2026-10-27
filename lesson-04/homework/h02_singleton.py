"""Домашнее задание. Тема 2: Singleton."""


class Capital:
    """Задание 05. Синглтон со сменой имени.

    Синглтон. Атрибут name изначально "не установлен"; метод rename(new_name)
    меняет имя — и это видно через любой вызов класса.

    Примеры:
        Capital() is Capital()
        Capital().name == "не установлен"
        Capital().rename("Пермь")
        Capital().name == "Пермь"
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте Capital.__new__")

    def rename(self, new_name):
        raise NotImplementedError("Реализуйте Capital.rename")


class Fibonacci:
    """Задание 06. Синглтон-генератор чисел Фибоначчи.

    Метод next() выдаёт очередное число последовательности: 0, 1, 1, 2, 3, 5, ...
    Состояние общее для всех «экземпляров». Не забудьте защиту от
    повторного __init__.

    Примеры:
        Fibonacci() is Fibonacci()
        a = Fibonacci()
        a.next() == 0
        a.next() == 1
        Fibonacci().next() == 1
        Fibonacci().next() == 2
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте Fibonacci.__new__")

    def next(self):
        raise NotImplementedError("Реализуйте Fibonacci.next")


class God:
    """Задание 07. Синглтон со счётчиком обращений.

    Синглтон. Классовый метод prayers() возвращает, сколько раз вызывался
    pray() (у любого «экземпляра» — счётчик общий).

    Примеры:
        God() is God()
        God.prayers() == 0
        God().pray()
        God().pray()
        God.prayers() == 2
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте God.__new__")

    def pray(self):
        raise NotImplementedError("Реализуйте God.pray")

    @classmethod
    def prayers(cls):
        raise NotImplementedError("Реализуйте God.prayers")
