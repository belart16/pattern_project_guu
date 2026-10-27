"""Домашнее задание. Тема 1: введение."""

MINI_GROUPS = {
    "порождающие": ["Singleton", "Builder", "Prototype"],
    "поведенческие": ["Observer", "Strategy", "Command"],
}


def hw_01(name):
    """Группа паттерна (малый словарь).

    Верните группу для name из MINI_GROUPS или None.

    Примеры:
        hw_01("Builder") == "порождающие"
        hw_01("Observer") == "поведенческие"
        hw_01("Adapter") is None
    """
    raise NotImplementedError("Реализуйте hw_01")


def hw_02():
    """Имена порождающих паттернов.

    Верните отсортированный список имён порождающих паттернов из словаря
    GROUPS файла tasks/t01_intro.py. Для проверки из корня репозитория
    запускайте модульно: python -i -m homework.h01_intro — тогда пакет
    tasks будет виден по импорту from tasks import t01_intro.

    Примеры:
        hw_02() == ["Abstract Factory", "Builder", "Factory Method", "Prototype", "Singleton"]
    """
    raise NotImplementedError("Реализуйте hw_02")


class Ticker:
    """Задание 03. Тикер: текущее и прошлое значение.

    tick(value) запоминает значение: оно становится текущим, а прежнее
    текущее — прошлым. current() возвращает текущее значение, previous() —
    прошлое (до первого тика оба None).

    Примеры:
        t = Ticker()
        t.current() is None
        t.previous() is None
        t.tick(10)
        t.current() == 10
        t.previous() is None
        t.tick(20)
        t.current() == 20
        t.previous() == 10
    """

    def tick(self, value):
        raise NotImplementedError("Реализуйте Ticker.tick")

    def current(self):
        raise NotImplementedError("Реализуйте Ticker.current")

    def previous(self):
        raise NotImplementedError("Реализуйте Ticker.previous")


def hw_04(name):
    """Намерение паттерна по имени.

    Обратный словарь к заданию 03 темы 1: верните формулировку-ключ по имени
    паттерна: "Singleton" → "единственный экземпляр", "Builder" →
    "пошаговая сборка сложного объекта", "Observer" → "уведомление подписчиков".
    Неизвестное имя — None.

    Примеры:
        hw_04("Singleton") == "единственный экземпляр"
        hw_04("Observer") == "уведомление подписчиков"
        hw_04("MVC") is None
    """
    raise NotImplementedError("Реализуйте hw_04")
