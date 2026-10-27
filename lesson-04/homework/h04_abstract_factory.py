"""Домашнее задание. Тема 4: Abstract Factory."""


class Header:
    """Продукт: заголовок темы theme."""

    def __init__(self, theme):
        self.theme = theme

    def render(self):
        return f"[{self.theme}] шапка"


class Footer:
    def __init__(self, theme):
        self.theme = theme

    def render(self):
        return f"[{self.theme}] подвал"


class LightPageFactory:
    """Задание 11, часть 1. Фабрика светлой страницы: theme = "light".

    create_header() → Header("light"); create_footer() → Footer("light").

    Примеры:
        LightPageFactory().create_header().render() == "[light] шапка"
        LightPageFactory().create_footer().render() == "[light] подвал"
    """

    def create_header(self):
        raise NotImplementedError("Реализуйте LightPageFactory.create_header")

    def create_footer(self):
        raise NotImplementedError("Реализуйте LightPageFactory.create_footer")


class DarkPageFactory:
    """Задание 11, часть 2. Фабрика тёмной страницы: theme = "dark".

    Примеры:
        DarkPageFactory().create_header().render() == "[dark] шапка"
        DarkPageFactory().create_footer().render() == "[dark] подвал"
    """

    def create_header(self):
        raise NotImplementedError("Реализуйте DarkPageFactory.create_header")

    def create_footer(self):
        raise NotImplementedError("Реализуйте DarkPageFactory.create_footer")


def hw_12(factory):
    """Задание 12. Клиентский код страницы.

    Верните строку из двух строк: заголовок и подвал, разделённые переводом
    строки ("\\n"), взяв продукты у фабрики.

    Примеры:
        hw_12(LightPageFactory()) == "[light] шапка\\n[light] подвал"
        hw_12(DarkPageFactory()) == "[dark] шапка\\n[dark] подвал"
    """
    raise NotImplementedError("Реализуйте hw_12")


class MobileMenu:
    """Продукт для задания 13."""

    def __init__(self):
        self.platform = "mobile"

    def show(self):
        return "меню: гамбургер"


class DesktopMenu:
    def __init__(self):
        self.platform = "desktop"

    def show(self):
        return "меню: панель сверху"


class MobileUIFactory:
    """Задание 13, часть 1. Фабрика мобильного интерфейса: create_menu() → MobileMenu.

    Примеры:
        MobileUIFactory().create_menu().show() == "меню: гамбургер"
        MobileUIFactory().create_menu().platform == "mobile"
    """

    def create_menu(self):
        raise NotImplementedError("Реализуйте MobileUIFactory.create_menu")


class DesktopUIFactory:
    """Задание 13, часть 2. Фабрика десктопного интерфейса: create_menu() → DesktopMenu.

    Примеры:
        DesktopUIFactory().create_menu().show() == "меню: панель сверху"
        DesktopUIFactory().create_menu().platform == "desktop"
    """

    def create_menu(self):
        raise NotImplementedError("Реализуйте DesktopUIFactory.create_menu")


def hw_14(first, second):
    """Задание 14. Согласованность тем двух фабрик.

    Верните True, если меню, созданные двумя фабриками, принадлежат одной
    платформе (атрибут platform одинаков), иначе False.

    Примеры:
        hw_14(MobileUIFactory(), MobileUIFactory()) == True
        hw_14(MobileUIFactory(), DesktopUIFactory()) == False
    """
    raise NotImplementedError("Реализуйте hw_14")
