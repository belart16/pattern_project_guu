"""Тема 2. Singleton: единственный экземпляр через __new__."""


class President:
    """Задание 07. Классический синглтон.

    Любой вызов President() возвращает ОДИН И ТОТ ЖЕ объект. Реализуйте
    через __new__ (создаёт и запоминает экземпляр в атрибуте класса),
    а __init__ пусть будет обычным. Атрибуты, установленные у одного
    «экземпляра», видны через любой другой вызов.

    Примеры:
        President() is President()
        p = President()
        p.name = "Ольга"
        President().name == "Ольга"
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте President.__new__")


class Database:
    """Задание 08. Синглтон с данными.

    Синглтон: все вызовы Database() дают один объект с внутренним словарём
    {"users": 42, "orders": 7}. Метод query(key) возвращает значение по ключу
    или None. Данные задаются при ПЕРВОМ создании и не пересоздаются
    при повторных вызовах класса.

    Примеры:
        Database() is Database()
        Database().query("users") == 42
        Database().query("orders") == 7
        Database().query("нет") is None
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте Database.__new__")

    def query(self, key):
        raise NotImplementedError("Реализуйте Database.query")


class State:
    """Задание 09. Ловушка повторного __init__ и её обход.

    Синглтон с изменяемым состоянием. Подводный камень: Python вызывает
    __init__ при КАЖДОМ вызове класса, даже когда __new__ вернул старый
    объект — наивный __init__ затрёт данные. Защитите инициализацию
    (например, через hasattr).

    Методы: set(key, value) и get(key, default=None).

    Примеры:
        State() is State()
        s1 = State()
        s1.set("x", 1)
        s2 = State()          # __init__ отработал ещё раз
        s2.get("x") == 1      # ...но данные не потерялись
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте State.__new__")

    def set(self, key, value):
        raise NotImplementedError("Реализуйте State.set")

    def get(self, key, default=None):
        raise NotImplementedError("Реализуйте State.get")


class IdGenerator:
    """Задание 10. Общий сквозной счётчик.

    Синглтон-генератор номеров: метод next() возвращает 1, 2, 3, ...
    Счётчик общий для всех «экземпляров» — сколько бы раз класс ни вызывали.

    Примеры:
        IdGenerator() is IdGenerator()
        a = IdGenerator()
        a.next() == 1
        b = IdGenerator()
        b.next() == 2
        a.next() == 3
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте IdGenerator.__new__")

    def next(self):
        raise NotImplementedError("Реализуйте IdGenerator.next")


class Universe:
    """Задание 11. Подсчёт вызовов конструктора.

    Синглтон, который знает, сколько раз его «создавали»: каждый вызов
    Universe() увеличивает счётчик класса (в том числе самый первый),
    но объект всегда один. Классовый метод creations() возвращает счётчик.

    Примеры:
        Universe(); Universe(); Universe()
        Universe.creations() == 3
        Universe() is Universe()
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте Universe.__new__")

    @classmethod
    def creations(cls):
        raise NotImplementedError("Реализуйте Universe.creations")


class License:
    """Задание 12. Синглтон с одноразовой выдачей.

    Синглтон. Метод assign(owner) выдаёт лицензию владельцу и запоминает
    его в атрибуте owner. Повторный вызов assign выбрасывает
    ValueError("лицензия уже выдана").

    Примеры:
        License() is License()
        lic = License()
        lic.assign("ООО Ромашка")
        lic.owner == "ООО Ромашка"
        License().assign("ООО Лютик")  # ValueError: лицензия уже выдана
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте License.__new__")

    def assign(self, owner):
        raise NotImplementedError("Реализуйте License.assign")
