# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Абстрактный класс для транспортных средств.

    Атрибуты:
    ----------
    make : str
        Марка транспортного средства.
    model : str
        Модель транспортного средства.
    year : int
        Год выпуска транспортного средства.

    Методы:
    --------
    start() -> str
        Запускает транспортное средство.
    stop() -> str
        Останавливает транспортное средство.
    honk() -> str
        Подает сигнал.

    Примеры:
    --------
    >>> vehicle = Vehicle("Toyota", "Corolla", 2020)  # Это вызовет ошибку, так как Vehicle абстрактный
    """

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self) -> str:
        """Запускает транспортное средство."""
        ...

    @abstractmethod
    def stop(self) -> str:
        """Останавливает транспортное средство."""
        ...

    @abstractmethod
    def honk(self) -> str:
        """Подает сигнал."""
        ...


class Furniture(ABC):
    """Абстрактный класс для мебели.

    Атрибуты:
    ----------
    material : str
        Материал мебели.
    dimensions : tuple
        Размеры мебели в формате (ширина, высота, глубина).

    Методы:
    --------
    assemble() -> str
        Собирает мебель.
    disassemble() -> str
        Разбирает мебель.
    move(new_location: str) -> str
        Перемещает мебель в новое место.

    Примеры:
    --------
    >>> furniture = Furniture("Wood", (100, 75, 50))  # Это вызовет ошибку, так как Furniture абстрактный
    """

    def __init__(self, material: str, dimensions: tuple):
        self.material = material
        self.dimensions = dimensions

    @abstractmethod
    def assemble(self) -> str:
        """Собирает мебель."""
        ...

    @abstractmethod
    def disassemble(self) -> str:
        """Разбирает мебель."""
        ...

    @abstractmethod
    def move(self, new_location: str) -> str:
        """Перемещает мебель в новое место."""
        ...


class Account(ABC):
    """Абстрактный класс для учетной записи.

    Атрибуты:
    ----------
    username : str
        Имя пользователя.
    email : str
        Электронная почта.
    balance : float
        Баланс учетной записи.

    Методы:
    --------
    deposit(amount: float) -> str
        Вносит деньги на счет.
    withdraw(amount: float) -> str
        Снимает деньги со счета.
    get_balance() -> float
        Возвращает текущий баланс.

    Примеры:
    --------
    >>> account = Account("john_doe", "john@example.com", 100.0)  # Это вызовет ошибку, так как Account абстрактный
    """

    def __init__(self, username: str, email: str, balance: float):
        self.username = username
        self.email = email
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: float) -> str:
        """Вносит деньги на счет."""
        ...

    @abstractmethod
    def withdraw(self, amount: float) -> str:
        """Снимает деньги со счета."""
        ...

    @abstractmethod
    def get_balance(self) -> float:
        """Возвращает текущий баланс."""
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()