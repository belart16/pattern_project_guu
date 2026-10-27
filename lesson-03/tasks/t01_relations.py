"""Тема 1. Принципы ООП: инкапсуляция, полиморфизм, отношения между объектами."""


class SecretNote:
    """Задание 01. Инкапсуляция: приватный атрибут и пин-код.

    Конструктор принимает текст заметки text и пин-код pin. Текст и пин-код
    храните «двойным подчёркиванием» (name mangling): __text и __pin — так
    атрибут недоступен снаружи как note.__text. Защищённый (одиночное
    подчёркивание) атрибут _attempts считает НЕУДАЧНЫЕ попытки доступа.

    Метод read(pin): при верном пин-коде возвращает текст; при неверном —
    ValueError("неверный пин-код") и увеличивает _attempts. Свойство attempts
    возвращает счётчик.

    Примеры:
        note = SecretNote("секрет", 1234)
        note.read(1234) == "секрет"
        note.attempts == 0
        note.read(9999)  # ValueError: неверный пин-код
        note.attempts == 1
        hasattr(note, "__text") == False
    """

    def __init__(self, text, pin):
        self.__text = text
        self.__pin = pin
        self._attempts = 0

    def read(self, pin):
        if pin == self.__pin:
            return self.__text
        else:
            self._attempts += 1
            raise ValueError("неверный пин-код")

    @property
    def attempts(self):
        return self._attempts


class Product:
    """Задание 02. Цена через свойство, скидка методом.

    Конструктор принимает name и price; цену храните в защищённом атрибуте
    _price. Свойство price доступно только для чтения. Метод
    apply_discount(percent) уменьшает цену на percent процентов и округляет
    результат до двух знаков (метод ничего не возвращает).

    Примеры:
        p = Product("чайник", 1000)
        p.price == 1000
        p.apply_discount(25)
        p.price == 750.0
        p.price = 1   # AttributeError: цена только для чтения
    """

    def __init__(self, name, price):
        self._price = price

    @property
    def price(self):
        return self._price

    def apply_discount(self, percent):
        self._price -= self._price * percent / 100
        self._price = round(self._price, 2)


def task_03(shapes):
    """Площадь любой коллекции фигур (duck typing).

    Верните сумму площадей всех объектов в shapes. У каждого объекта есть
    метод area() — БЕЗ проверки типов: если объект «крякает как утка»
    (умеет area), он подходит. Это и есть полиморфизм Python.

    Примеры:
        class Circle:
            def __init__(self, r): self.r = r
            def area(self): return 3.14159 * self.r ** 2
        class Square:
            def __init__(self, a): self.a = a
            def area(self): return self.a ** 2

        task_03([Circle(1), Square(2)]) == 3.14159 + 4
        task_03([]) == 0
    """
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area


class Driver:
    """Задание 04, часть 1. Водитель."""

    def __init__(self, name):
        self.name = name


class Car:
    """Задание 04, часть 2. Ассоциация: машина и водитель существуют независимо.

    Метод assign_driver(driver) запоминает водителя (в атрибут driver;
    изначально None). Метод drive(): если водитель не назначен — строка
    "припаркована"; иначе "{имя водителя} ведёт {модель}".

    Примеры:
        car = Car("Жигули")
        car.drive() == "припаркована"
        car.assign_driver(Driver("Иван"))
        car.drive() == "Иван ведёт Жигули"
    """

    def __init__(self, model):
        self.model = model
        self.driver = None

    def assign_driver(self, driver):
        self.driver = driver

    def drive(self):
        if self.driver is None:
            return "припаркована"
        else:
            return f"{self.driver.name} ведёт {self.model}"


class Employee:
    """Задание 05, часть 1. Сотрудник с именем."""

    def __init__(self, name):
        self.name = name


class Department:
    """Задание 05, часть 2. Агрегация: отдел СОДЕРЖИТ сотрудников,
    но они создаются снаружи и живут своей жизнью.

    Метод add(employee) добавляет ссылку на сотрудника; метод names()
    возвращает список имён в порядке добавления. Сотрудник, переданный
    в отдел, остаётся тем же самым объектом (проверьте через is).

    Примеры:
        dept = Department("ИТ")
        anna = Employee("Анна")
        dept.add(anna)
        dept.names() == ["Анна"]
        dept.add(Employee("Борис"))
        dept.names() == ["Анна", "Борис"]
    """

    def __init__(self, name):
        self.name = name
        self.employees = []
        
    def add(self, employee):
        self.employees.append(employee)

    def names(self):
        return [employee.name for employee in self.employees]


class Room:
    """Задание 06, часть 1. Комната с названием."""

    def __init__(self, title):
        self.title = title


class House:
    """Задание 06, часть 2. Композиция: дом СОЗДАЁТ свои комнаты,
    они не существуют без него.

    Конструктор принимает количество комнат rooms_count и сам создаёт
    комнаты с названиями "комната 1", "комната 2", ... Свойство rooms
    возвращает список комнат.

    Примеры:
        h = House(3)
        [r.title for r in h.rooms] == ["комната 1", "комната 2", "комната 3"]
        h2 = House(2)
        h.rooms[0] is not h2.rooms[0]   # у каждого дома свои комнаты
    """

    def __init__(self, rooms_count):
        self._rooms = [Room(f"комната {i + 1}") for i in range(rooms_count)]

    @property
    def rooms(self):
        return self._rooms
