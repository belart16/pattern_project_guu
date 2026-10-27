"""Тема 2. Композиция: «has-a», делегирование, внедрение зависимостей."""


class Engine:
    """Задание 07, часть 1. Двигатель с мощностью power (л. с.).

    Метод start() возвращает строку "двигатель запущен".
    """

    def __init__(self, power):
        self.power = power

    def start(self):
        return "двигатель запущен"


class Car:
    """Задание 07, часть 2. Машина СОДЕРЖИТ двигатель (композиция).

    Конструктор принимает model и engine. Метод start() делегирует вызов
    двигателю. Свойство horsepower возвращает мощность двигателя
    (тоже через делегирование).

    Примеры:
        car = Car("Жигули", Engine(150))
        car.horsepower == 150
        car.start() == "двигатель запущен"
    """

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    @property
    def horsepower(self):
        return self.engine.power

    def start(self):
        return self.engine.start()


class Address:
    """Задание 08, часть 1. Адрес: город, улица, дом."""

    def __init__(self, city, street, house):
        self.city = city
        self.street = street
        self.house = house


class Person:
    """Задание 08, часть 2. Человек с адресом (композиция).

    Метод full_address() возвращает строку "{город}, {улица}, {дом}".

    Примеры:
        p = Person("Анна", Address("Москва", "Тверская", 1))
        p.full_address() == "Москва, Тверская, 1"
    """

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def full_address(self):
        return f"{self.address.city}, {self.address.street}, {self.address.house}"


class Chapter:
    """Задание 09, часть 1. Глава: название title и число страниц pages."""

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


class Manual:
    """Задание 09, часть 2. Справочник из глав.

    Метод add(chapter) добавляет главу; total_pages() возвращает суммарное
    число страниц; longest_chapter() — название главы с наибольшим числом
    страниц (при равенстве — первая добавленная).

    Примеры:
        m = Manual("справка")
        m.add(Chapter("Введение", 10))
        m.add(Chapter("Детали", 25))
        m.add(Chapter("Итоги", 25))
        m.total_pages() == 60
        m.longest_chapter() == "Детали"
    """

    def __init__(self, title):
        self.title = title
        self.chapters = []

    def add(self, chapter):
        self.chapters.append(chapter)

    def total_pages(self):
        return sum(chapter.pages for chapter in self.chapters)

    def longest_chapter(self):
        return max(self.chapters, key=lambda chapter: chapter.pages).title


class Service:
    """Задание 10. Сервис с внедрённым логгером (внедрение зависимости).

    Конструктор принимает name и logger — любой объект с методом
    log(message). Метод run(x) логирует "старт: {x}", возвращает
    "готово: {x}" и логирует "финиш: {x}".

    Примеры:
        class FakeLogger:
            def __init__(self): self.messages = []
            def log(self, message): self.messages.append(message)

        logger = FakeLogger()
        Service("импорт", logger).run(5) == "готово: 5"
        logger.messages == ["старт: 5", "финиш: 5"]
    """

    def __init__(self, name, logger):
        self.name = name
        self.logger = logger

    def run(self, x):
        self.logger.log(f"старт: {x}")
        result = f"готово: {x}"
        self.logger.log(f"финиш: {x}")
        return result


class Track:
    """Задание 11, часть 1. Трек: название и длительность в секундах."""

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Playlist:
    """Задание 11, часть 2. Плейлист содержит треки.

    Метод add(track) добавляет трек; total_duration() — суммарная длительность
    в секундах; find(title) возвращает объект Track с этим названием
    или None.

    Примеры:
        pl = Playlist("дорога")
        pl.add(Track("песня 1", 120))
        pl.add(Track("песня 2", 180))
        pl.total_duration() == 300
        pl.find("песня 1").duration == 120
        pl.find("нет такой") is None
    """

    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def total_duration(self):
        return sum(track.duration for track in self.tracks)

    def find(self, title):
        for track in self.tracks:
            if track.title == title:
                return track
        return None


class Item:
    """Задание 12, часть 1. Товар: цена за штуку price и количество quantity."""

    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    """Задание 12, часть 2. Корзина товаров.

    Метод add(item) добавляет товар; total() возвращает суммарную стоимость
    (цена * количество, просуммированная по корзине); most_expensive()
    возвращает товар с наибольшей ценой ЗА ШТУКУ.

    Примеры:
        cart = Cart()
        cart.add(Item("ручка", 20, 5))
        cart.add(Item("книга", 500))
        cart.total() == 600
        cart.most_expensive().name == "книга"
    """

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price * item.quantity for item in self.items)

    def most_expensive(self):
        return max(self.items, key=lambda item: item.price)
