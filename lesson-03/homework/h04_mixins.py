"""Домашнее задание. Тема 4: миксины и MRO."""


class DescribeMixin:
    """Задание 11. Строковое описание объекта.

    Метод describe() возвращает "ClassName: имя1=значение1, имя2=значение2"
    по всем атрибутам экземпляра (self.__dict__), имя класса — через
    type(self).__name__.

    Примеры:
        class Point(DescribeMixin):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        Point(1, 2).describe() == "Point: x=1, y=2"
    """

    def describe(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}: {attrs}"


class EqMixin:
    """Задание 12. Сравнение по полям (шаблонный метод).

    Класс-носитель реализует fields() — кортеж ИМЁН атрибутов для
    сравнения. Миксин определяет __eq__(other): True, только если other —
    экземпляр того же класса и все поля совпадают.

    Класс Book(title, author) наследует EqMixin, fields() → ("title", "author").

    Примеры:
        Book("а", "X") == Book("а", "X")
        Book("а", "X") != Book("б", "X")
        Book("а", "X") == "а"   # False: другой тип
    """

    def fields(self):
        raise NotImplementedError("Носитель миксина должен реализовать fields()")

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return all(getattr(self, field) == getattr(other, field) for field in self.fields())


class Book(EqMixin):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def fields(self):
        return ("title", "author")


class P:
    """Задание 13. Ромб MRO: S→Q→R→P.

    Четыре класса: P; Q(P); R(P); S(Q, R). Метод who(): P возвращает "P";
    каждый следующий — "{буква}->" плюс super().who(). MRO класса S
    даёт порядок обхода S → Q → R → P.

    Примеры:
        P().who() == "P"
        Q().who() == "Q->P"
        R().who() == "R->P"
        S().who() == "S->Q->R->P"
    """

    def who(self):
        return "P"


class Q(P):
    def who(self):
        return f"Q->" + super().who()


class R(P):
    def who(self):
        return f"R->" + super().who()


class S(Q, R):
    def who(self):
        return f"S->" + super().who()


class StatsMixin:
    """Задание 14. Ленивое состояние в миксине (без __init__).

    Метод remember(value) при первом вызове создаёт список _log
    и добавляет значение. Метод average() возвращает среднее по _log
    (float) или 0, если запоминаний ещё не было.

    Примеры:
        class Sensor(StatsMixin):
            def __init__(self, name):
                self.name = name

        s = Sensor("датчик")
        s.average() == 0
        s.remember(2); s.remember(4)
        s.average() == 3.0
        s2 = Sensor("другой")
        s2.average() == 0        # состояние независимое
    """

    def remember(self, value):
        if not hasattr(self, '_log'):
            self._log = []
        self._log.append(value)

    def average(self):
        if not hasattr(self, '_log'):
            return 0
        return sum(self._log) / len(self._log)
