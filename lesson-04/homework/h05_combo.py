"""Домашнее задание. Тема 5: порождающие вместе."""


class Settings:
    """Задание 15. Синглтон с настройками по умолчанию.

    Синглтон: все вызовы Settings() — один объект. При первом создании
    словарь настроек наполняется значениями по умолчанию:
    {"тема": "светлая", "язык": "ru"}. Методы set(key, value) и
    get(key, default=None) — общие для всего приложения.

    Примеры:
        Settings() is Settings()
        Settings().get("тема") == "светлая"
        Settings().set("тема", "тёмная")
        Settings().get("тема") == "тёмная"
        Settings().get("нет", 0) == 0
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте Settings.__new__")

    def set(self, key, value):
        raise NotImplementedError("Реализуйте Settings.set")

    def get(self, key, default=None):
        raise NotImplementedError("Реализуйте Settings.get")


def hw_16(func):
    """Задание 16. Фабрика считающих обёрток.

    Верните обёртку, которая считает свои вызовы в атрибуте calls
    (изначально 0) и пробрасывает результат func.

    Примеры:
        calls = []
        def side_effect(x):
            calls.append(x)
            return x + 1

        wrapped = hw_16(side_effect)
        wrapped.calls == 0
        wrapped(1) == 2
        wrapped(2) == 3
        wrapped.calls == 2
        calls == [1, 2]
    """
    raise NotImplementedError("Реализуйте hw_16")


class Cache:
    """Задание 17. Синглтон-кэш.

    Синглтон с общим кэшем: put(key, value) сохраняет; get(key) возвращает
    значение или None. Кэш один для всего приложения (защита от повторного
    __init__ обязательна).

    Примеры:
        Cache() is Cache()
        Cache().put("a", 1)
        Cache().get("a") == 1
        Cache().get("нет") is None
    """

    def __new__(cls):
        raise NotImplementedError("Реализуйте Cache.__new__")

    def put(self, key, value):
        raise NotImplementedError("Реализуйте Cache.put")

    def get(self, key):
        raise NotImplementedError("Реализуйте Cache.get")
