"""Домашнее задание. Тема 1: инкапсуляция и отношения."""


class Safe:
    """Задание 01. Сейф: приватность и счётчик попыток.

    Конструктор принимает код code. Внутренности храните с двойным
    подчёркиванием (name mangling). Метод open(code): верный код —
    возвращает "открыто"; неверный — ValueError("неверный код") и
    увеличивает защищённый счётчик _attempts. Свойство attempts
    возвращает число неудачных попыток.

    Примеры:
        s = Safe(777)
        s.open(777) == "открыто"
        s.attempts == 0
        s.open(111)  # ValueError: неверный код
        s.attempts == 1
        hasattr(s, "__code") == False
    """

    def __init__(self, code):
        self.__code = code
        self._attempts = 0

    def open(self, code):
        if code == self.__code:
            return "открыто"
        else:
            self._attempts += 1
            raise ValueError("неверный код")

    @property
    def attempts(self):
        return self._attempts


class Config:
    """Задание 02. Настройки только для чтения.

    Конструктор принимает произвольные именованные настройки (**settings)
    и хранит их во внутреннем словаре. Свойство settings возвращает словарь
    (можно копию) и НЕ имеет сеттера. Изменения — только через метод
    update(key, value); метод get(key, default=None) читает значение.

    Примеры:
        c = Config(theme="dark", lang="ru")
        c.settings == {"theme": "dark", "lang": "ru"}
        c.get("theme") == "dark"
        c.get("missing", 0) == 0
        c.update("lang", "en")
        c.get("lang") == "en"
        c.settings = {}   # AttributeError
    """

    def __init__(self, **settings):
        self.__settings = settings

    @property
    def settings(self):
        return self.__settings.copy()

    def update(self, key, value):
        self.__settings[key] = value

    def get(self, key, default=None):
        return self.__settings.get(key, default)


class Player:
    """Задание 03, часть 1. Игрок."""

    def __init__(self, name):
        self.name = name


class Team:
    """Задание 03, часть 2. Агрегация: команда из игроков.

    add(player) запоминает игрока; roster() возвращает имена в порядке
    добавления. Игроки создаются снаружи и остаются теми же объектами.

    Примеры:
        t = Team("звёзды")
        anna = Player("Анна")
        t.add(anna)
        t.roster() == ["Анна"]
        t.add(Player("Борис"))
        t.roster() == ["Анна", "Борис"]
    """

    def __init__(self, name):
        self.name = name
        self._players = []

    def add(self, player):
        self._players.append(player)

    def roster(self):
        return [player.name for player in self._players]


class Course:
    """Задание 04. Ассоциация: курс и записавшиеся студенты.

    enroll(student) добавляет студента; students() возвращает имена
    в порядке записи. У студента есть атрибут name.

    Примеры:
        c = Course("Python")
        c.enroll(Student("Анна"))
        c.enroll(Student("Борис"))
        c.students() == ["Анна", "Борис"]
    """

    def __init__(self, title):
        self.title = title
        self._students = []

    def enroll(self, student):
        self._students.append(student)

    def students(self):
        return [student.name for student in self._students]


class Student:
    """Студент (для задания 04)."""

    def __init__(self, name):
        self.name = name
