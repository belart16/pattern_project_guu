"""Домашнее задание. Тема 2: композиция и делегирование."""


class BoatEngine:
    """Задание 05, часть 1. Лодочный двигатель.

    Конструктор принимает мощность hp. Метод start() возвращает
    "двигатель заведён".
    """

    def __init__(self, hp):
        self.hp = hp

    def start(self):
        return "двигатель заведён"


class Boat:
    """Задание 05, часть 2. Лодка делегирует запуск двигателю.

    sail() возвращает "{имя лодки}: {результат запуска двигателя}".

    Примеры:
        Boat("Волга", BoatEngine(90)).sail() == "Волга: двигатель заведён"
    """

    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def sail(self):
        return f"{self.name}: {self.engine.start()}"

class Page:
    """Задание 06, часть 1. Страница: заголовок и число слов."""

    def __init__(self, title, words):
        self.title = title
        self.words = words


class Notebook:
    """Задание 06, часть 2. Блокнот из страниц.

    add_page(page) добавляет страницу; total_words() — суммарное число
    слов; longest_page() — заголовок страницы с наибольшим числом слов
    (при равенстве — первая добавленная).

    Примеры:
        n = Notebook()
        n.add_page(Page("титул", 0))
        n.add_page(Page("текст", 100))
        n.total_words() == 100
        n.longest_page() == "текст"
    """

    def __init__(self):
        self._pages = []

    def add_page(self, page):
        self._pages.append(page)

    def total_words(self):
        return sum(page.words for page in self._pages)

    def longest_page(self):
        return max(self._pages, key=lambda page: page.words).title


class Greeter:
    """Задание 07. Приветствия с внедрённым логгером.

    Конструктор принимает logger — любой объект с методом log(message).
    Метод greet(name) логирует "приветствие: {name}" и возвращает
    "Привет, {name}!".

    Примеры:
        class FakeLogger:
            def __init__(self): self.messages = []
            def log(self, message): self.messages.append(message)

        logger = FakeLogger()
        Greeter(logger).greet("Анна") == "Привет, Анна!"
        logger.messages == ["приветствие: Анна"]
    """

    def __init__(self, logger):
        self.logger = logger

    def greet(self, name):
        self.logger.log(f"приветствие: {name}")
        return f"Привет, {name}!"
