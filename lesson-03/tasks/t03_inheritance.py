"""Тема 3. Наследование: «is-a», переопределение, super(), атрибуты класса."""


class Animal:
    """Задание 13. Базовый класс и переопределение метода.

    Конструктор принимает name. Метод speak() возвращает "неизвестный звук".
    Подклассы Dog и Cat переопределяют speak(): Dog — "гав", Cat — "мяу".
    Атрибут name инициализируется только в базовом классе.

    Примеры:
        Animal("существо").speak() == "неизвестный звук"
        Dog("Рекс").speak() == "гав"
        Cat("Мурка").speak() == "мяу"
        Dog("Рекс").name == "Рекс"
    """

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "неизвестный звук"


class Dog(Animal):
    def speak(self):
        return "гав"



class Cat(Animal):
    def speak(self):
        return "мяу"


class Employee:
    """Задание 14. super() в __init__.

    Конструктор Employee: name и salary, оба — атрибуты.
    Manager наследует Employee и добавляет team_size: его __init__ вызывает
    super().__init__(...) для общих атрибутов. Метод Manager.team()
    возвращает "команда из {team_size}".

    Примеры:
        m = Manager("Ольга", 90000, 5)
        m.name == "Ольга"
        m.salary == 90000
        m.team_size == 5
        isinstance(m, Employee) == True
        m.team() == "команда из 5"
    """

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def team(self):
        return f"команда из {self.team_size}"

class Vehicle:
    """Задание 15. super() в переопределённом методе.

    Vehicle: конструктор с max_speed; drive() возвращает
    "еду со скоростью {max_speed}".
    ElectricCar наследует Vehicle, добавляет battery (ёмкость, кВт·ч);
    его drive() вызывает super().drive() и дополняет строку:
    "{базовая строка} (электро, запас {battery} кВт·ч)".

    Примеры:
        Vehicle(120).drive() == "еду со скоростью 120"
        ElectricCar(120, 60).drive() == "еду со скоростью 120 (электро, запас 60 кВт·ч)"
    """

    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        return f"еду со скоростью {self.max_speed}"


class ElectricCar(Vehicle):
    def __init__(self, max_speed, battery):
        super().__init__(max_speed)
        self.battery = battery

    def drive(self):
        return f"{super().drive()} (электро, запас {self.battery} кВт·ч)"


class Employee2:
    """Задание 16. Переопределение расчёта с super().

    Employee2: name и salary; метод monthly_pay() возвращает salary.
    SalesEmployee наследует Employee2, добавляет sales (объём продаж)
    и rate (доля бонуса); его monthly_pay() возвращает результат
    super().monthly_pay() ПЛЮС sales * rate.

    Примеры:
        Employee2("Иван", 50000).monthly_pay() == 50000
        SalesEmployee("Анна", 50000, 200000, 0.05).monthly_pay() == 60000.0
    """

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary


class SalesEmployee(Employee2):
    def __init__(self, name, salary, sales, rate):
        super().__init__(name, salary)
        self.sales = sales
        self.rate = rate

    def monthly_pay(self):
        return super().monthly_pay() + self.sales * self.rate


class SortedList(list):
    """Задание 17. Наследование от встроенного типа.

    Список, который остаётся отсортированным по возрастанию: переопределите
    append(item) так, чтобы элемент вставлялся в правильную позицию
    (остальные методы list не трогайте).

    Примеры:
        s = SortedList()
        s.append(3); s.append(1); s.append(2)
        s == [1, 2, 3]
        isinstance(s, list) == True
        s.append(0)  # вставится в начало
        s == [0, 1, 2, 3]
    """

    def append(self, item):
        
        index = 0
        while index < len(self) and self[index] < item:
            index += 1
        
        super().insert(index, item)


class Worker:
    """Задание 18. Трёхуровневая цепочка наследования.

    Worker(name).describe() возвращает "{name} работает".
    OfficeWorker(Worker) переопределяет describe(): super().describe()
    плюс " в офисе". Director(OfficeWorker) — super().describe() плюс
    ", руководит". Каждый уровень дописывает свою часть через super().

    Примеры:
        Worker("Иван").describe() == "Иван работает"
        OfficeWorker("Ольга").describe() == "Ольга работает в офисе"
        Director("Пётр").describe() == "Пётр работает в офисе, руководит"
        isinstance(Director("П"), Worker) == True
    """

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} работает"

class OfficeWorker(Worker):
    def describe(self):
        return f"{super().describe()} в офисе"

class Director(OfficeWorker):
    def describe(self):
        return f"{super().describe()}, руководит"


class Transport:
    """Задание 19. Переопределение атрибута КЛАССА.

    Атрибут класса wheels = 4. Метод info() возвращает
    "колёс: {self.wheels}" — Python ищет wheels сначала в экземпляре,
    затем в классе и его родителях. Подкласс Bike переопределяет wheels
    как атрибут СВОЕГО класса (wheels = 2), не трогая метод.

    Примеры:
        Transport().info() == "колёс: 4"
        Bike().info() == "колёс: 2"
        Transport.wheels == 4
        Bike.wheels == 2
        "wheels" not in vars(Transport())   # у экземпляра своего атрибута нет
    """

    wheels = 4

    def info(self):
        return f"колёс: {self.wheels}"


class Bike(Transport):
    wheels = 2


class Wallet:
    """Задание 20. Расширение: подкласс умеет всё, что умеет родитель.

    Wallet.__init__: balance = 0. Метод add(amount) увеличивает баланс.
    BonusWallet(Wallet): __init__ вызывает super().__init__() и добавляет
    bonus = 0; метод add_bonus(points) увеличивает bonus. Метод add
    наследуется БЕЗ переопределения.

    Примеры:
        w = Wallet(); w.add(100); w.balance == 100
        bw = BonusWallet()
        bw.add(100)          # унаследованный метод работает
        bw.balance == 100
        bw.add_bonus(5)
        bw.bonus == 5
        bw2 = BonusWallet(); bw2.balance == 0   # экземпляры независимы
    """

    def __init__(self):
        self.balance = 0

    def add(self, amount):
        self.balance += amount


class BonusWallet(Wallet):
    def __init__(self):
        super().__init__()
        self.bonus = 0

    def add_bonus(self, points):
        self.bonus += points


class Bird:
    """Задание 21. Переопределение с другим поведением + полиморфизм.

    Bird.fly() возвращает "лечу". Penguin(Bird) переопределяет fly() —
    "не умею летать": подкласс имеет право вести себя иначе, при этом
    остаётся птицей. Функция task_21(birds) возвращает список результатов
    fly() для каждого объекта — без проверок типов.

    Примеры:
        Bird().fly() == "лечу"
        Penguin().fly() == "не умею летать"
        task_21([Bird(), Penguin()]) == ["лечу", "не умею летать"]
        isinstance(Penguin(), Bird) == True
    """

    def fly(self):
        return "лечу"


class Penguin(Bird):
    def fly(self):
        return "не умею летать"


def task_21(birds):
    return [bird.fly() for bird in birds]


def task_22(animals):
    """Задание 22. Фильтрация по типу: isinstance.

    Верните список имён только тех объектов animals, которые являются
    экземплярами класса Dog (задание 13), в исходном порядке.
    Используйте isinstance — он признаёт и подклассов Dog, если бы они были.

    Примеры:
        task_22([Dog("Рекс"), Cat("Мурка"), Dog("Шарик"), Animal("Кто")])
            == ["Рекс", "Шарик"]
        task_22([]) == []
    """
    return [animal.name for animal in animals if isinstance(animal, Dog)]


class Polygon:
    """Задание 23. Базовый конкретный метод + «хук» для подкласса.

    Конструктор принимает список сторон sides. Метод perimeter() ВОЗВРАЩАЕТ
    сумму сторон — он готов и наследуется как есть. Метод name() — «хук»:
    в базовом классе возбуждает NotImplementedError("переопределите name"),
    а Triangle(Polygon) переопределяет его строкой "треугольник".

    Примеры:
        Polygon([1, 1]).perimeter() == 2
        Triangle([3, 4, 5]).perimeter() == 12     # унаследован без изменений
        Triangle([3, 4, 5]).name() == "треугольник"
        Polygon([1, 1]).name()  # NotImplementedError: переопределите name
    """

    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def name(self):
        raise NotImplementedError("переопределите name")


class Triangle(Polygon):
    def name(self):
        return "треугольник"


def task_24(employees):
    """Задание 24. Расчёт зарплат полиморфно.

    Верните список кортежей (name, monthly_pay()) для каждого сотрудника.
    Функция не должна проверять типы: она работает с ЛЮБЫМ объектом,
    у которого есть атрибут name и метод monthly_pay() — базовым это
    даёт зарплату, менеджерам по продажам — зарплату с бонусом.

    Примеры:
        task_24([Employee2("Иван", 50000),
                 SalesEmployee("Анна", 50000, 200000, 0.05)])
            == [("Иван", 50000), ("Анна", 60000.0)]
        task_24([]) == []
    """
    return [(employee.name, employee.monthly_pay()) for employee in employees]
