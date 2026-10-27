"""Тема 5. Абстрактные классы и интерфейсы (модуль abc)."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Задание 31. Базовый абстрактный класс.

    Shape — абстрактный класс с абстрактным методом area().
    Реализуйте подклассы Circle(r) и Rectangle(w, h), вычисляющие площадь.
    Экземпляр Shape создать нельзя.

    Примеры:
        Shape()   # TypeError: абстрактный класс
        Circle(2).area() == 4 * math.pi
        Rectangle(3, 4).area() == 12
    """

    @abstractmethod
    def area(self):
        raise NotImplementedError("Реализуйте Shape.area")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        raise NotImplementedError("Реализуйте Circle.area")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        raise NotImplementedError("Реализуйте Rectangle.area")


class Animal(ABC):
    """Задание 32. Конкретный метод на абстрактной базе (шаблонный метод).

    Абстрактный метод speak(); конкретный метод introduce() возвращает
    "Я говорю: {speak()}" — он готов к работе, как только подкласс
    реализует speak(). Подкласс Cat: speak() → "мяу".

    Примеры:
        Cat("Мурка").introduce() == "Я говорю: мяу"
        Animal("X")   # TypeError: speak не реализован
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        raise NotImplementedError("Реализуйте Animal.speak")

    def introduce(self):
        raise NotImplementedError("Реализуйте Animal.introduce")


class Cat(Animal):
    def speak(self):
        raise NotImplementedError("Реализуйте Cat.speak")


class Vehicle(ABC):
    """Задание 33. Абстрактное свойство.

    Vehicle объявляет абстрактное СВОЙСТВО max_speed (через
    @property + @abstractmethod). Подкласс Car реализует его константой 220.

    Примеры:
        Vehicle()   # TypeError
        Car("Лада").max_speed == 220
    """

    @property
    @abstractmethod
    def max_speed(self):
        raise NotImplementedError("Реализуйте Vehicle.max_speed")


class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    @property
    def max_speed(self):
        raise NotImplementedError("Реализуйте Car.max_speed")


class Plugin(ABC):
    """Задание 34. Реестр подклассов.

    Абстрактный run(). Классовый метод subclasses() возвращает отсортированный
    список имён ПРЯМЫХ подклассов того класса, у которого вызван
    (cls.__subclasses__()).

    Примеры:
        class Echo(Plugin):
            def run(self): return "echo"

        "Echo" in Plugin.subclasses()
        Echo().run() == "echo"
    """

    @abstractmethod
    def run(self):
        raise NotImplementedError("Реализуйте Plugin.run")

    @classmethod
    def subclasses(cls):
        raise NotImplementedError("Реализуйте Plugin.subclasses")


class Serializable(ABC):
    """Задание 35, часть 1. Интерфейс сериализации."""

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError("Реализуйте Serializable.to_dict")


def task_35(items):
    """Задание 35, часть 2. Работа через интерфейс, а не через тип.

    Верните список словарей для всех items, вызывая to_dict(). Функция
    принимает любые объекты, реализующие интерфейс Serializable, —
    без isinstance-проверок.

    Примеры:
        class Book(Serializable):
            def __init__(self, title):
                self.title = title
            def to_dict(self):
                return {"title": self.title}

        task_35([Book("а"), Book("б")]) == [{"title": "а"}, {"title": "б"}]
        task_35([]) == []
    """
    raise NotImplementedError("Реализуйте task_35")


class Item:
    """Задание 36, часть 1. Предмет: имя и стоимость (из упражнения 3 книги)."""

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Box(ABC):
    """Задание 36, часть 2. Абстрактная коробка (по упражнению 3 книги).

    Абстрактные методы:
      add(item)  — положить предмет;
      empty()    — забрать ВСЕ предметы и вернуть их списком;
      count()    — сколько предметов сейчас в коробке.

    Реализуйте два подкласса с разным внутренним хранением:
      ListBox  — хранит предметы в списке;
      DictBox  — хранит в словаре.
    """

    @abstractmethod
    def add(self, item):
        raise NotImplementedError("Реализуйте Box.add")

    @abstractmethod
    def empty(self):
        raise NotImplementedError("Реализуйте Box.empty")

    @abstractmethod
    def count(self):
        raise NotImplementedError("Реализуйте Box.count")


class ListBox(Box):
    def add(self, item):
        raise NotImplementedError("Реализуйте ListBox.add")

    def empty(self):
        raise NotImplementedError("Реализуйте ListBox.empty")

    def count(self):
        raise NotImplementedError("Реализуйте ListBox.count")


class DictBox(Box):
    def add(self, item):
        raise NotImplementedError("Реализуйте DictBox.add")

    def empty(self):
        raise NotImplementedError("Реализуйте DictBox.empty")

    def count(self):
        raise NotImplementedError("Реализуйте DictBox.count")


def task_36(*boxes):
    """Задание 36, часть 3. Переупаковка коробок (по книге).

    Соберите все предметы из всех коробок и распределите их между коробками
    как можно равнее (первые коробки могут получить на один предмет больше).
    Порядок предметов не важен. Функция работает с ЛЮБЫМИ подклассами Box.

    Примеры:
        b1, b2, b3 = ListBox(), ListBox(), DictBox()
        # ... 20, 9 и 5 предметов ...
        task_36(b1, b2, b3)
        sorted(b.count() for b in (b1, b2, b3)) == [11, 11, 12]
    """
    raise NotImplementedError("Реализуйте task_36")
