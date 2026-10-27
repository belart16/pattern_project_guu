"""Тема 3. Фабричные функции и Factory Method."""

import math


class Car:
    """Продукт: автомобиль."""

    name = "автомобиль"


class Truck:
    name = "грузовик"


class Bike:
    name = "мотоцикл"


class Ship:
    name = "судно"


class Circle:
    """Продукт: круг радиуса r."""

    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rect:
    """Продукт: прямоугольник."""

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


def task_13(kind):
    """Функция-фабрика.

    Верните объект по строке kind: "car" → Car, "truck" → Truck,
    "bike" → Bike. Для неизвестного kind — ValueError("неизвестный транспорт").

    Примеры:
        task_13("car").name == "автомобиль"
        isinstance(task_13("bike"), Bike)
        task_13("train")  # ValueError: неизвестный транспорт
    """
    raise NotImplementedError("Реализуйте task_13")


class TransportFactory:
    """Задание 14. Фабричный метод класса.

    Классовый метод create(kind) делает то же, что task_13: возвращает
    Car/Truck/Bike по строке, при неизвестном kind — ValueError.

    Примеры:
        TransportFactory.create("truck").name == "грузовик"
        isinstance(TransportFactory.create("car"), Car)
        TransportFactory().create("bike").name == "мотоцикл"   # и через экземпляр
    """

    @classmethod
    def create(cls, kind):
        raise NotImplementedError("Реализуйте TransportFactory.create")


class Logistics:
    """Задание 15. Канонический Factory Method.

    Базовый класс доставки: метод deliver() ВОЗВРАЩАЕТ строку
    "{имя транспорта} доставляет груз", беря транспорт у фабричного метода
    create_transport(). Сам create_transport() в базовом классе — «хук»:
    возбуждает NotImplementedError("выберите тип логистики").

    Подклассы RoadLogistics и SeaLogistics переопределяют ТОЛЬКО
    create_transport(): Road → Car, Sea → Ship.

    Примеры:
        RoadLogistics().deliver() == "автомобиль доставляет груз"
        SeaLogistics().deliver() == "судно доставляет груз"
        Logistics().create_transport()  # NotImplementedError: выберите тип логистики
    """

    def create_transport(self):
        raise NotImplementedError("выберите тип логистики")

    def deliver(self):
        raise NotImplementedError("Реализуйте Logistics.deliver")


class RoadLogistics(Logistics):
    def create_transport(self):
        raise NotImplementedError("Реализуйте RoadLogistics.create_transport")


class SeaLogistics(Logistics):
    def create_transport(self):
        raise NotImplementedError("Реализуйте SeaLogistics.create_transport")


class ShapeFactory:
    """Задание 16. Реестр классов-продуктов.

    Фабрика с регистрацией: register(name, cls) запоминает класс продукта;
    create(name, **kwargs) создаёт экземпляр зарегистрированного класса
    с переданными аргументами. Неизвестное имя — ValueError("неизвестный продукт").

    Примеры:
        f = ShapeFactory()
        f.register("circle", Circle)
        c = f.create("circle", r=2)
        isinstance(c, Circle)
        c.area() == 4 * math.pi
        f.create("hexagon")  # ValueError: неизвестный продукт
    """

    def __init__(self):
        raise NotImplementedError("Реализуйте ShapeFactory.__init__")

    def register(self, name, cls):
        raise NotImplementedError("Реализуйте ShapeFactory.register")

    def create(self, name, **kwargs):
        raise NotImplementedError("Реализуйте ShapeFactory.create")


def task_17(rule):
    """Фабрика функций.

    Верните функцию одного аргумента value:
      "positive" → value > 0
      "even"     → value % 2 == 0
      "nonempty" → bool(value)
    Неизвестное правило — ValueError("неизвестное правило").

    Примеры:
        task_17("positive")(5) == True
        task_17("positive")(-1) == False
        task_17("even")(4) == True
        task_17("nonempty")("") == False
        task_17("odd")  # ValueError: неизвестное правило
    """
    raise NotImplementedError("Реализуйте task_17")


def task_18(shape, **params):
    """Параметризованная фабрика.

    Создайте фигуру по имени и параметрам:
      "circle" → Circle(r=...)
      "rect"   → Rect(w=..., h=...)
      "square" → Rect(w=s, h=s) по одному параметру side
    Неизвестное имя — ValueError("неизвестная фигура").

    Примеры:
        task_18("circle", r=2).area() == 4 * math.pi
        task_18("rect", w=3, h=4).area() == 12
        task_18("square", side=5).area() == 25
    """
    raise NotImplementedError("Реализуйте task_18")
