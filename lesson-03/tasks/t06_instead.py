"""Тема 6. Наследование vs композиция: стратегии, делегирование, правила."""


class Formatter:
    """Задание 37. Стратегия-функция.

    Конструктор принимает необязательную strategy — функцию str → str
    (по умолчанию None, что означает «без преобразований»). Метод
    set_strategy(strategy) заменяет стратегию на ходу. Метод render(text)
    применяет текущую стратегию к text и возвращает результат.

    Примеры:
        f = Formatter()
        f.render("привет") == "привет"
        f.set_strategy(str.upper)
        f.render("привет") == "ПРИВЕТ"
        f.set_strategy(lambda s: s[::-1])
        f.render("привет") == "тевирп"
    """

    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def render(self, text):
        if self.strategy is None:
            return text
        return self.strategy(text)


class SortAscending:
    """Задание 38. Стратегии-классы.

    Каждый класс-стратегия имеет метод sort(data), возвращающий НОВЫЙ
    отсортированный список: SortAscending — по возрастанию,
    SortDescending — по убыванию.

    Sorter(strategy) хранит стратегию; его метод sort(data) делегирует
    работу стратегии. Стратегию можно передать другую, не трогая Sorter.

    Примеры:
        Sorter(SortAscending()).sort([3, 1, 2]) == [1, 2, 3]
        Sorter(SortDescending()).sort([3, 1, 2]) == [3, 2, 1]
    """

    def sort(self, data):
        return sorted(data)


class SortDescending:
    def sort(self, data):
        return sorted(data, reverse=True)


class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)


class WalkMode:
    """Задание 39. Поведение, заменяемое на ходу.

    WalkMode.move() → "иду"; FlyMode.move() → "лечу".
    Robot(name) принимает режим mode; его move() делегирует режиму;
    set_mode(mode) меняет поведение без пересоздания робота.

    Примеры:
        robot = Robot("R2", WalkMode())
        robot.move() == "иду"
        robot.set_mode(FlyMode())
        robot.move() == "лечу"
    """

    def move(self):
        return "иду"


class FlyMode:
    def move(self):
        return "лечу"


class Robot:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def set_mode(self, mode):
        self.mode = mode

    def move(self):
        return self.mode.move()


class ConsoleChannel:
    """Задание 40. Каналы уведомлений: делегирование.

    ConsoleChannel.send(message) → "[консоль] {message}";
    EmailChannel.send(message) → "[почта] {message}".
    NotificationSender(channel).send(message) полностью делегирует отправку
    каналу и возвращает его результат.

    Примеры:
        NotificationSender(ConsoleChannel()).send("привет") == "[консоль] привет"
        NotificationSender(EmailChannel()).send("привет") == "[почта] привет"
    """

    def send(self, message):
        return f"[консоль] {message}"


class EmailChannel:
    def send(self, message):
        return f"[почта] {message}"


class NotificationSender:
    def __init__(self, channel):
        self.channel = channel

    def send(self, message):
        return self.channel.send(message)


class Validator:
    """Задание 41. Правила как объекты (композиция поведений).

    Конструктор принимает rules — список пар (имя_правила, функция-предикат).
    Предикат принимает проверяемое значение и возвращает True/False.
    Метод validate(value) возвращает СПИСОК ИМЁН правил, которые значение
    НАРУШИЛО (предикат вернул False), в исходном порядке правил.

    Примеры:
        v = Validator([
            ("positive", lambda x: x > 0),
            ("even", lambda x: x % 2 == 0),
        ])
        v.validate(4) == []
        v.validate(3) == ["even"]
        v.validate(-4) == ["positive"]
        v.validate(-3) == ["positive", "even"]
    """

    def __init__(self, rules):
        self.rules = rules

    def validate(self, value):
        return [
            name
            for name, predicate in self.rules
            if not predicate(value)
        ]


class Learner:
    """Задание 42. Person с делегированием (по упражнению 4 книги).

    Learner хранит список courses; метод enrol(course) добавляет курс.
    Teacher хранит courses_taught; метод assign_teaching(course) добавляет.

    Person(name, learner=None, teacher=None) хранит оба компонента
    (по умолчанию их нет). Методы-обёртки:
      enrol(course)          — делегирует learner.enrol; если learner нет —
                               RuntimeError("нет компонента learner");
      assign_teaching(course)— делегирует teacher.assign_teaching; если
                               teacher нет — RuntimeError("нет компонента teacher").

    Примеры:
        jane = Person("Джейн", learner=Learner(), teacher=Teacher())
        jane.enrol("python")
        jane.assign_teaching("math")
        jane.learner.courses == ["python"]
        jane.teacher.courses_taught == ["math"]

        bob = Person("Боб")
        bob.enrol("python")   # RuntimeError: нет компонента learner
    """

    def __init__(self):
        self.courses = []

    def enrol(self, course):
        self.courses.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, learner=None, teacher=None):
        self.name = name
        self.learner = learner
        self.teacher = teacher

    def enrol(self, course):
        if self.learner is None:
            raise RuntimeError("нет компонента learner")
        self.learner.enrol(course)

    def assign_teaching(self, course):
        if self.teacher is None:
            raise RuntimeError("нет компонента teacher")
        self.teacher.assign_teaching(course)
