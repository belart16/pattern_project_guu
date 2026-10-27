"""Тема 4. Множественное наследование, миксины и MRO."""

import json


class JSONMixin:
    """Задание 25. Миксин сериализации в JSON.

    Метод to_json() возвращает JSON-строку всех атрибутов экземпляра
    (self.__dict__) с ensure_ascii=False.

    Примеры:
        class Model(JSONMixin):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        m = Model(1, 2)
        json.loads(m.to_json()) == {"x": 1, "y": 2}
    """

    def to_json(self):
        raise NotImplementedError("Реализуйте JSONMixin.to_json")


class ReprMixin:
    """Задание 26. Миксин универсального __repr__.

    __repr__ возвращает "ClassName(имя1=значение1, имя2=значение2, ...)"
    по всем атрибутам экземпляра. Имя класса возьмите через
    type(self).__name__.

    Примеры:
        class Point(ReprMixin):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        repr(Point(1, 2)) == "Point(x=1, y=2)"
    """

    def __repr__(self):
        raise NotImplementedError("Реализуйте ReprMixin.__repr__")


class Point(ReprMixin, JSONMixin):
    """Задание 27. Комбинирование миксинов.

    Наследуйте Point от двух миксинов сразу (ReprMixin и JSONMixin)
    и убедитесь, что работают оба поведения. Конструктор принимает x и y.

    Примеры:
        p = Point(1, 2)
        repr(p) == "Point(x=1, y=2)"
        json.loads(p.to_json()) == {"x": 1, "y": 2}
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class A:
    """Задание 28. Ромб наследования и MRO.

    Реализуйте четыре класса: A; B(A); C(A); D(B, C). У каждого — метод
    who(). A возвращает "A"; каждый следующий возвращает "{буква}->"
    плюс результат super().who(). Благодаря MRO вызов D().who() обойдёт
    классы в порядке D → B → C → A.

    Примеры:
        A().who() == "A"
        B().who() == "B->A"
        C().who() == "C->A"
        D().who() == "D->B->C->A"
    """

    def who(self):
        raise NotImplementedError("Реализуйте A.who")


class B(A):
    def who(self):
        raise NotImplementedError("Реализуйте B.who")


class C(A):
    def who(self):
        raise NotImplementedError("Реализуйте C.who")


class D(B, C):
    def who(self):
        raise NotImplementedError("Реализуйте D.who")


class TimestampMixin:
    """Задание 29. Миксин с состоянием (без __init__!).

    Миксины обычно не определяют __init__, чтобы не конфликтовать с классом-
    носителем. Метод stamp(): при первом вызове лениво создаёт атрибут
    _stamps (0), увеличивает его на 1 и возвращает новое значение.

    Примеры:
        class Doc(TimestampMixin):
            def __init__(self, title):
                self.title = title

        d = Doc("отчёт")
        d.stamp() == 1
        d.stamp() == 2
        d2 = Doc("письмо")
        d2.stamp() == 1        # счётчики независимы
    """

    def stamp(self):
        raise NotImplementedError("Реализуйте TimestampMixin.stamp")


class ComparableMixin:
    """Задание 30. Миксин-шаблон: сравнение через key().

    Класс-носитель должен реализовать метод key() — «шаблонный метод»,
    по которому сравниваются объекты. Миксин определяет:
      __lt__(other): self.key() < other.key()
      __eq__(other): self.key() == other.key()
    Если key() не реализован носителем — пусть возбуждается NotImplementedError.

    Класс Price наследует ComparableMixin: конструктор с value,
    key() возвращает value.

    Примеры:
        prices = [Price(3), Price(1), Price(2)]
        [p.value for p in sorted(prices)] == [1, 2, 3]
        Price(10) == Price(10)
        Price(10) != Price(20)
    """

    def key(self):
        raise NotImplementedError("Носитель миксина должен реализовать key()")

    def __lt__(self, other):
        raise NotImplementedError("Реализуйте ComparableMixin.__lt__")

    def __eq__(self, other):
        raise NotImplementedError("Реализуйте ComparableMixin.__eq__")


class Price(ComparableMixin):
    def __init__(self, value):
        self.value = value

    def key(self):
        raise NotImplementedError("Реализуйте Price.key")
