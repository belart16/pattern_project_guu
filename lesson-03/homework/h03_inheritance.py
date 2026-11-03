"""Домашнее задание. Тема 3: наследование и super()."""


class PersonA:
    """Задание 08. super() в переопределённом методе.

    PersonA(name).introduce() возвращает "Меня зовут {name}".
    StudentA(name, university) переопределяет introduce(), ВЫЗЫВАЯ
    super().introduce() и дописывая ", учусь в {university}".

    Примеры:
        PersonA("Иван").introduce() == "Меня зовут Иван"
        StudentA("Иван", "МГУ").introduce() == "Меня зовут Иван, учусь в МГУ"
    """

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Меня зовут {self.name}"


class StudentA(PersonA):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    def introduce(self):
        return f"{super().introduce()}, учусь в {self.university}"


class BaseAccount:
    """Задание 09. Сберегательный счёт.

    BaseAccount(owner, balance): баланс — свойство balance (только
    чтение), метод deposit(amount) пополняет счёт.
    SavingsAccount(owner, balance, rate) добавляет rate (проценты в год);
    метод add_interest() увеличивает баланс на rate процентов (округление
    до двух знаков) и возвращает новый баланс.

    Примеры:
        acc = SavingsAccount("Анна", 1000, 5)
        acc.balance == 1000
        acc.add_interest() == 1050.0
        acc.balance == 1050.0
        acc.deposit(50)
        acc.balance == 1100.0
    """

    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount


class SavingsAccount(BaseAccount):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self._rate = rate

    def add_interest(self):
        interest = self._balance * self._rate / 100
        self._balance += interest
        return round(self._balance, 2)


class QueueList(list):
    """Задание 10. Очередь на базе встроенного list.

    Наследуйте list и реализуйте очередь:
      enqueue(item) — в конец;
      dequeue()     — из начала (для пустой очереди — естественный IndexError);
      front()       — первый элемент без извлечения;
      size()        — число элементов.

    Примеры:
        q = QueueList()
        isinstance(q, list) == True
        q.enqueue("первый"); q.enqueue("второй")
        q.size() == 2
        q.front() == "первый"
        q.dequeue() == "первый"
        q.dequeue() == "второй"
        q.dequeue()  # IndexError
    """

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)

    def front(self):
        return self[0]

    def size(self):
        return len(self)
