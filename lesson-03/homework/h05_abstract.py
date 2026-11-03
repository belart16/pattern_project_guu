"""Домашнее задание. Тема 5: абстрактные классы."""

from abc import ABC, abstractmethod


class SoundSource(ABC):
    """Задание 15. Шаблонный метод на абстрактной базе.

    Абстрактный make_sound(); конкретный speak(times=1) возвращает
    звуки, разделённые пробелами: make_sound() ровно times раз.
    Подкласс DogSound: make_sound() → "гав".

    Примеры:
        DogSound().speak() == "гав"
        DogSound().speak(3) == "гав гав гав"
        SoundSource()   # TypeError
    """

    @abstractmethod
    def make_sound(self):
        pass

    def speak(self, times=1):
        return " ".join(self.make_sound() for _ in range(times))


class DogSound(SoundSource):
    def make_sound(self):
        return "гав"


class Storage(ABC):
    """Задание 16, часть 1. Интерфейс хранилища.

    Абстрактные save(key, value) и load(key). Реализуйте MemoryStorage
    на словаре: load несуществующего ключа возвращает None.

    Примеры:
        st = MemoryStorage()
        st.save("a", 1)
        st.load("a") == 1
        st.load("нет") is None
    """

    @abstractmethod
    def save(self, key, value):
        pass

    @abstractmethod
    def load(self, key):
        pass


class MemoryStorage(Storage):
    def __init__(self):
        self._data = {}

    def save(self, key, value):
        self._data[key] = value

    def load(self, key):
        return self._data.get(key)

class Sealed:
    """Задание 17. Запрет наследования.

    Реализуйте класс Sealed так, чтобы ЛЮБАЯ попытка унаследоваться от него
    возбуждала TypeError при определении подкласса. Подсказка: метод
    __init_subclass__. Сам Sealed должен спокойно создаваться.

    Примеры:
        Sealed()          # работает
        class Child(Sealed): pass   # TypeError
    """

    def __init_subclass__(cls, **kwargs):
        raise TypeError("Наследование от Sealed запрещено")
